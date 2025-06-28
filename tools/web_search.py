from langchain.tools import tool
import requests

@tool
def search_web(query: str) -> str:
    """
    Search the web using DuckDuckGo and return a summary or related result.
    """
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1"
        response = requests.get(url).json()

        if response.get("Abstract"):
            return response["Abstract"]

        # Try related topics
        topics = response.get("RelatedTopics", [])
        if topics:
            return topics[0].get("Text", "No relevant result found.")

        return "No relevant information found."
    except Exception as e:
        return f"Search error: {e}"
