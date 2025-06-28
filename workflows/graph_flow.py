from typing_extensions import TypedDict
from typing import Union
from langgraph.graph import StateGraph, END
from agents.planner import plan_tasks
from agents.executor import execute_task
from agents.evaluator import evaluate_result
from langchain_core.runnables import RunnableConfig

class PlannerState(TypedDict):
    goal: str
    tasks: list
    current_task_index: int
    current_result: str
    results: list
    retry: bool
    __end__: bool

def build_graph():
    def planner_node(state: PlannerState) -> dict:
        subtasks = plan_tasks(state["goal"])
        return {
            "tasks": subtasks,
            "current_task_index": 0,
            "results": [],
            "retry": False,
            "__end__": False
        }

    def executor_node(state: PlannerState) -> dict:
        task = state["tasks"][state["current_task_index"]]
        return {
            "current_result": execute_task(task),
            "retry": False  # Clear retry flag before each evaluation
        }

    def evaluator_node(state: PlannerState) -> dict:
        idx = state["current_task_index"]
        task = state["tasks"][idx]
        result = state["current_result"]
        verdict = evaluate_result(task, result).strip()

        needs_retry = verdict in {"⚠️ Needs Review", "❌ Incomplete"}

        new_results = state["results"] + [{
            "task": task,
            "result": result,
            "verdict": verdict
        }]

        next_idx = idx if needs_retry else idx + 1
        done = next_idx >= len(state["tasks"])

        return {
            "results": new_results,
            "current_task_index": next_idx,
            "retry": needs_retry,
            "__end__": done
        }

    def route_from_evaluator(state: PlannerState) -> str | None:
        if state.get("__end__") or state["current_task_index"] >= len(state["tasks"]):
            return END
        return "executor"

    graph = StateGraph(PlannerState)
    graph.add_node("planner", planner_node)
    graph.add_node("executor", executor_node)
    graph.add_node("evaluator", evaluator_node)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "evaluator")
    graph.add_conditional_edges("evaluator", route_from_evaluator)

    return graph.compile()
