from workflows.graph_flow import build_graph
from memory.vector_store import store_result

if __name__ == "__main__":
    goal = input("🎯 Describe your goal: ")

    # Run the agentic workflow
    state = {"goal": goal}
    graph = build_graph()
    final_state = graph.invoke(state)

    print("\n✅ Final Results:\n")
    for i, r in enumerate(final_state["results"], 1):
        print(f"{i}. {r['task']}")
        print(f"   → 🧠 {r['result'].strip()}")
        print(f"   → 🔍 Evaluation: {r['verdict']}\n")

    # Store result to FAISS
    store_result(goal, final_state["results"])
    print("📦 Results stored in memory.")