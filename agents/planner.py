from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
import json
import re

llm = OllamaLLM(model="mistral")

# Prompt to break goals into tasks
planner_prompt = PromptTemplate(
    input_variables=["goal"],
    template="""
You are a helpful assistant that breaks down a user's goal into specific tasks.
Return only a JSON object like this:
{{
  "Task List": [
    "task 1",
    "task 2",
    "task 3"
  ]
}}

Goal: {goal}

Subtasks:
"""
)

def plan_tasks(user_goal: str):
    prompt = planner_prompt.format(goal=user_goal)
    result = llm.invoke(prompt)

    # Try to extract JSON from the response
    try:
        json_text = re.search(r'\{[\s\S]+\}', result).group()
        parsed = json.loads(json_text)
        return parsed["Task List"]
    except Exception as e:
        print("❌ Error parsing JSON:", e)
        print("Raw output:\n", result)
        return []
