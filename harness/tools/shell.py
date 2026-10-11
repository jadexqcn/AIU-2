"""Shell 命令执行工具"""
import subprocess


def run_shell(command: str) -> dict:
    """执行 shell 命令并返回输出"""
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=30
        )
        output = result.stdout if result.stdout else ""
        error = result.stderr if result.stderr else ""
        return {
            "command": command,
            "exit_code": result.returncode,
            "stdout": output[:2000],
            "stderr": error[:500]
        }
    except subprocess.TimeoutExpired:
        return {"error": "命令执行超时（30秒）"}
    except Exception as e:
        return {"error": str(e)}


def register(registry):
    registry["run_shell"] = {
        "name": "run_shell",
        "description": "执行 shell 命令并返回输出结果",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "要执行的命令"}
            },
            "required": ["command"]
        },
        "handler": run_shell
    }
