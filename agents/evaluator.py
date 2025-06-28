from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model="mistral")

evaluator_prompt = PromptTemplate(
    input_variables=["task", "result"],
    template="""
You are a critical evaluator of assistant task execution results.
Given a task and the assistant's response, assess how well it completed the task.

Respond ONLY with one of the following verdicts:
✅ Good - if the task was completed well
⚠️ Needs Review - if the answer is incomplete or might have issues
❌ Incomplete - if the task was poorly handled or misunderstood

Task: {task}
Assistant Response: {result}

Verdict:
"""
)

def evaluate_result(task: str, result: str) -> str:
    prompt = evaluator_prompt.format(task=task, result=result)
    verdict = llm.invoke(prompt)
    return verdict.strip()
