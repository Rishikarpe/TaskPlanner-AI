# 🧠 TaskPlanner-AI

A LangGraph-based intelligent agent system that:
- 🎯 Plans tasks based on a user goal
- 🤖 Executes them using a local LLM (Mistral 7B via Ollama)
- 🧪 Evaluates the results step-by-step

Built using:
- 🧩 LangGraph
- 🧠 Local LLMs (via Ollama)
- 🌐 Streamlit for UI

---

## ✅ Prerequisites

To run this project locally with **Mistral 7B**, follow these steps:

### 1. Install Docker

- Download and install Docker from:  
  👉 https://www.docker.com/products/docker-desktop  
- Ensure Docker is running.

---

### 2. Install Ollama

Install Ollama (used to run local LLMs):

---

### 3. Pull the Mistral 7B Model:
ollama pull mistral 

---

### 4. Run Ollama:
ollama serve

---

### 5. Install dependencies
pip install -r requirements.txt

---

### 6. Start the app
streamlit run ui/app.py
