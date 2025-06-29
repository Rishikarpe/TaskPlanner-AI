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

---

#OUTPUT
![Thinking](https://github.com/user-attachments/assets/b2ce0b51-16d7-4c7e-b509-a7cf3445ca10)
![Output4](https://github.com/user-attachments/assets/3d635ce7-c914-42d1-9f6a-9c7e22d693f9)
![Output3](https://github.com/user-attachments/assets/e69d3e02-8696-4ffe-96b3-7a60f67339c1)
![Output2](https://github.com/user-attachments/assets/d499b2a9-270f-41f3-8ba2-0388ac6cae5a)
![Output1](https://github.com/user-attachments/assets/d889063e-de28-4445-8db4-95c1d9b1efbf)
