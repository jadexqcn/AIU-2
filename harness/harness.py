"""
Harness - 轻量级 AI Agent 执行框架
参考 Pi Agent 架构: Agent = Model + Harness
"""
import json
import os
import sys
import urllib.request

TOOLS = {}


def load_tools(tools_dir):
    if not os.path.exists(tools_dir):
        return
    for f in os.listdir(tools_dir):
        if f.endswith(".py") and not f.startswith("_"):
            name = f[:-3]
            try:
                mod = __import__(f"tools.{name}", fromlist=[name])
                if hasattr(mod, "register"):
                    mod.register(TOOLS)
                    print(f"  + {name}")
            except Exception as e:
                print(f"  ! {name}: {e}")


def chat(messages, tools_schema):
    payload = {
        "model": "qwen3:8b",
        "messages": messages,
        "stream": False,
        "options": {"num_ctx": 8192},
    }
    if tools_schema:
        payload["tools"] = tools_schema
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "http://127.0.0.1:11434/api/chat",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())


def run_tool_call(tool_name, arguments):
    if tool_name not in TOOLS:
        return {"error": f"未知工具: {tool_name}"}
    try:
        return TOOLS[tool_name]["handler"](**arguments)
    except Exception as e:
        return {"error": str(e)}


def main():
    print("=" * 50)
    print("  Harness - AI Agent 执行框架")
    print("  模型: qwen3:8b (本地 Ollama)")
    print("=" * 50)
    print()

    print("加载工具:")
    load_tools(os.path.join(os.path.dirname(__file__), "tools"))
    print(f"共 {len(TOOLS)} 个工具\n")

    tools_schema = [
        {
            "type": "function",
            "function": {
                "name": t["name"],
                "description": t["description"],
                "parameters": t["parameters"],
            },
        }
        for t in TOOLS.values()
    ]

    system_prompt = "你是 Harness 框架中的 AI 助手。你可以调用工具完成任务。"
    messages = [{"role": "system", "content": system_prompt}]

    print("开始对话 (输入 /exit 退出)\n")

    while True:
        try:
            user_input = input("用户: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见!")
            break

        if not user_input:
            continue
        if user_input.lower() == "/exit":
            print("再见!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            resp = chat(messages, tools_schema)
        except Exception as e:
            print(f"[错误] {e}")
            messages.pop()
            continue

        msg = resp.get("message", {})
        content = msg.get("content", "")
        tool_calls = msg.get("tool_calls", [])

        # 处理工具调用
        if tool_calls:
            for tc in tool_calls:
                func = tc.get("function", {})
                tool_name = func.get("name")
                arguments = func.get("arguments", {})
                print(f"\n[调用工具] {tool_name}")
                result = run_tool_call(tool_name, arguments)
                print(f"[工具结果] {json.dumps(result, ensure_ascii=False)[:200]}\n")

                messages.append({"role": "assistant", "tool_calls": [tc]})
                messages.append({
                    "role": "tool",
                    "content": json.dumps(result, ensure_ascii=False),
                    "name": tool_name,
                })

            # 让模型基于工具结果继续回复
            try:
                resp2 = chat(messages, None)
                content = resp2.get("message", {}).get("content", "")
            except Exception as e:
                content = f"[获取工具结果回复失败] {e}"

        if content:
            print(f"助手: {content}\n")
            messages.append({"role": "assistant", "content": content})
        else:
            print("助手: (无回复)\n")


if __name__ == "__main__":
    main()
