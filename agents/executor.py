from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType

# Import tools
from tools.python_tool import run_python
from tools.translate_tool import translate_text
from tools.web_search import search_web

# LLMs
llm_suggester = OllamaLLM(model="mistral")
llm_tool_user = OllamaLLM(model="mistral") 

# Prompt-only executor
executor_prompt = PromptTemplate(
    input_variables=["task"],
    template="""
You are an intelligent assistant that helps users complete tasks.

Task: {task}

Provide a short, helpful response or suggestion to execute this task.
"""
)

# Tool registration
tools = [
    Tool(name="PythonExecutor", func=run_python, description="Evaluate Python/math expressions"),
    Tool(name="Translator", func=translate_text, description="Translate text to Hindi"),
    Tool(name="DuckDuckGoSearch", func=search_web, description="Search the web using DuckDuckGo"),
]

# Tool agent
tool_agent = initialize_agent(
    tools,
    llm_tool_user,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

def execute_task(task: str) -> str:
    """
    First, try giving a helpful suggestion using LLM.
    If the task looks like something a tool can do (e.g., math, translate, search), let the agent handle it.
    """
    try:
        if any(keyword in task.lower() for keyword in [
            "calculate", "+", "-", "*", "/", "evaluate", "python",
            "sum", "difference", "translate", "search", "find", "lookup"
        ]):
            return tool_agent.run(task)

        prompt = executor_prompt.format(task=task)
        return llm_suggester.invoke(prompt)

    except Exception as e:
        return f"⚠️ Error during execution: {e}"
