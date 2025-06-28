# tools/python_tool.py

from langchain.tools import tool

@tool
def run_python(code: str) -> str:
    """
    Executes a simple Python expression or math calculation and returns the result.
    Example: '2 + 2' → '4'
    """
    try:
        result = eval(code, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error: {e}"
