# Harness - AI Agent 执行框架

轻量级 AI Agent 框架，参考 Pi Agent 架构：`Agent = Model + Harness`

## 快速开始

### 1. 启动 Ollama

```powershell
ollama serve
```

### 2. 运行 Harness

```bash
python harness.py
```

### 3. 对话示例

```
用户: 计算 2+3*4
助手: [调用工具] calculate
[工具结果] {"result": 14}
助手: 2+3*4 = 14

用户: 列出当前目录的文件
助手: [调用工具] list_files
助手: 当前目录包含: harness.py, README.md, tools/
```

## 内置工具

- `calculate` - 数学计算
- `list_files` - 列出目录
- `read_file` / `write_file` - 文件读写
- `run_shell` - 执行命令

## 添加工具

在 `tools/` 下创建 Python 文件，实现 `register(registry)` 函数：

```python
def my_tool(param: str) -> dict:
    return {"result": "done"}

def register(registry):
    registry["my_tool"] = {
        "name": "my_tool",
        "description": "工具描述",
        "parameters": {
            "type": "object",
            "properties": {"param": {"type": "string"}},
            "required": ["param"]
        },
        "handler": my_tool
    }
```