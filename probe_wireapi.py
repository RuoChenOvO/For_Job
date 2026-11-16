import argparse, json, os, time, sys, urllib.request, urllib.error

def call(url, key, body, timeout=60):
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
        method="POST",
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode("utf-8", "replace")
            return r.status, raw, time.time() - t0, None
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        return e.code, raw, time.time() - t0, f"HTTPError {e.code}"
    except Exception as e:
        return None, "", time.time() - t0, repr(e)

def extract_text(wire, raw):
    """尽力从两种 wire_api 的响应里取出正文与 finish 信息。"""
    try:
        d = json.loads(raw)
    except Exception:
        return {"text": raw[:1000], "finish_reason": None, "usage": None, "note": "非JSON响应"}
    if wire == "responses":
        txt = d.get("output_text")
        if not txt:
            parts = []
            for item in d.get("output", []) or []:
                for c in item.get("content", []) or []:
                    if c.get("type") in ("output_text", "text"):
                        parts.append(c.get("text", ""))
            txt = "".join(parts)
        return {"text": txt, "status": d.get("status"),
                "finish_reason": d.get("incomplete_details") or d.get("status"),
                "usage": d.get("usage"), "note": None}
    else:
        ch = (d.get("choices") or [{}])[0]
        return {"text": (ch.get("message") or {}).get("content", ""),
                "finish_reason": ch.get("finish_reason"),
                "usage": d.get("usage"), "note": None}

REFUSAL_MARKERS = ["I'm sorry, I can't assist", "I can’t assist", "I can't help with", "I cannot assist"]

def is_refusal(text, finish, payload_note):
    if not text or not text.strip():
        return True
    for m in REFUSAL_MARKERS:
        if m.lower() in text.lower():
            return True
    if finish in ("content_filter",):
        return True
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--model", default="gpt-4o")
    ap.add_argument("--prompt-file", help="原始 SafeMem 规划提示文件路径")
    ap.add_argument("--prompt", default="请用一句话介绍大熊猫。")
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--out", default="wireapi_results.json")
    args = ap.parse_args()

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        print("错误：环境变量 OPENAI_API_KEY 未设置", file=sys.stderr)
        sys.exit(2)

    prompt = open(args.prompt_file, encoding="utf-8").read() if args.prompt_file else args.prompt
    base = args.base_url.rstrip("/")

    # ===== 这里替换成你的原规划提示要求 JSON 的部分 =====
    instruction = (
        "\n\n请严格按以下 JSON 格式输出，不要输出任何其他文字：\n"
        '{"action": "TOGGLE_OFF", "target": "<对象名>"}'
    )
    full_prompt = prompt + instruction

    results = []

    # ---- 1) chat/completions ----
    body_chat = {
        "model": args.model,
        "max_tokens": args.max_tokens,
        "messages": [{"role": "user", "content": full_prompt}],
    }
    st, raw, lat, err = call(base + "/chat/completions", key, body_chat)
    e = extract_text("chat", raw)
    results.append({
        "wire_api": "chat/completions", "http_status": st, "latency_s": round(lat, 2),
        "refused": is_refusal(e["text"], e.get("finish_reason"), e.get("note")),
        "finish_reason": e.get("finish_reason"), "text": e["text"], "error": err,
        "raw_head": raw[:500],
    })
    print(f"[chat/completions] status={st} latency={lat:.2f}s refused={results[-1]['refused']}")

    time.sleep(2)

    # ---- 2) responses ----
    body_resp = {
        "model": args.model,
        "max_output_tokens": args.max_tokens,
        "input": full_prompt,
    }
    st, raw, lat, err = call(base + "/responses", key, body_resp)
    e = extract_text("responses", raw)
    results.append({
        "wire_api": "responses", "http_status": st, "latency_s": round(lat, 2),
        "refused": is_refusal(e["text"], e.get("finish_reason"), e.get("note")),
        "finish_reason": e.get("finish_reason"), "text": e["text"], "error": err,
        "raw_head": raw[:500],
    })
    print(f"[responses]        status={st} latency={lat:.2f}s refused={results[-1]['refused']}")

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n结果已写入 {args.out}")

    # 结论提示
    a, b = results[0], results[1]
    if a["http_status"] and b["http_status"] and a["refused"] != b["refused"]:
        print(">>> 两个 wire_api 结果不同：拒答很可能来自某一侧的请求/转换层，而不是模型本身。")
    elif a["refused"] and b["refused"]:
        print(">>> 两者都拒：更偏向模型层或中转对两种格式都做了共同处理。")
    else:
        print(">>> 两者都通：这次没复现，需要多跑几次确认稳定性。")

if __name__ == "__main__":
    main()