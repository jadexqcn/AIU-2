"""文件操作工具"""
import os


def list_files(path: str = ".") -> dict:
    """列出指定目录下的文件和文件夹"""
    try:
        items = os.listdir(path)
        files = []
        dirs = []
        for item in items:
            full = os.path.join(path, item)
            if os.path.isdir(full):
                dirs.append(item)
            else:
                files.append(item)
        return {"path": path, "files": files, "directories": dirs}
    except Exception as e:
        return {"error": str(e)}


def read_file(path: str) -> dict:
    """读取文本文件内容"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"path": path, "content": content[:2000]}
    except Exception as e:
        return {"error": str(e)}


def write_file(path: str, content: str) -> dict:
    """写入文本文件"""
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return {"path": path, "written": True}
    except Exception as e:
        return {"error": str(e)}


def register(registry):
    registry["list_files"] = {
        "name": "list_files",
        "description": "列出目录下的文件和文件夹",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "目录路径"}
            },
            "required": []
        },
        "handler": list_files
    }
    registry["read_file"] = {
        "name": "read_file",
        "description": "读取文本文件内容",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "文件路径"}
            },
            "required": ["path"]
        },
        "handler": read_file
    }
    registry["write_file"] = {
        "name": "write_file",
        "description": "写入文本文件",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "文件路径"},
                "content": {"type": "string", "description": "文件内容"}
            },
            "required": ["path", "content"]
        },
        "handler": write_file
    }
