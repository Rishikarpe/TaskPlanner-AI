import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.docstore.document import Document

VECTOR_DIR = "memory/faiss_db"

def get_embedding_model():
    return OllamaEmbeddings(model="mistral")

def load_vector_store() -> FAISS:
    index_file = os.path.join(VECTOR_DIR, "index.faiss")
    if os.path.exists(index_file):
        return FAISS.load_local(VECTOR_DIR, get_embedding_model(), allow_dangerous_deserialization=True)
    else:
        # Initialize with a dummy document to avoid failure
        dummy_doc = Document(page_content="Initialization Document", metadata={"type": "init"})
        vectorstore = FAISS.from_documents([dummy_doc], get_embedding_model())
        vectorstore.save_local(VECTOR_DIR)
        return vectorstore

def store_result(goal: str, results: list[dict]):
    vectorstore = load_vector_store()
    docs = []

    for r in results:
        metadata = {"goal": goal, "task": r["task"], "verdict": r["verdict"]}
        content = f"Goal: {goal}\nTask: {r['task']}\nResult: {r['result']}\nVerdict: {r['verdict']}"
        docs.append(Document(page_content=content, metadata=metadata))

    vectorstore.add_documents(docs)
    vectorstore.save_local(VECTOR_DIR)

def search_similar_tasks(query: str, top_k: int = 3):
    vectorstore = load_vector_store()
    results = vectorstore.similarity_search(query, k=top_k)
    return [doc for doc in results if "task" in doc.metadata and "verdict" in doc.metadata]

def save_task_result(task: str, results: list[dict]):
    """Store a task + its results as embeddings in the vector DB."""
    vectorstore = load_vector_store()

    # Convert list of dicts to formatted strings
    result_strings = []
    for r in results:
        content = f"Task: {r.get('task', task)}\nResult: {r.get('result', '')}\nVerdict: {r.get('verdict', '')}"
        result_strings.append(content)

    full_result = "\n\n".join(result_strings)

    vectorstore.add_texts(
        texts=[full_result],
        metadatas=[{"task": task, "verdict": full_result}]
    )

    vectorstore.save_local(VECTOR_DIR)
