"""计算器工具"""


def calculate(expression: str) -> dict:
    """计算数学表达式，支持加减乘除、幂运算等"""
    try:
        allowed = set("0123456789+-*/.() %**//")
        if not all(c in allowed for c in expression):
            return {"error": "表达式包含非法字符"}
        result = eval(expression)
        return {"expression": expression, "result": result}
    except Exception as e:
        return {"error": str(e)}


def register(registry):
    registry["calculate"] = {
        "name": "calculate",
        "description": "计算数学表达式",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "数学表达式，如 2+3*4"
                }
            },
            "required": ["expression"]
        },
        "handler": calculate
    }
