from langchain.document_loaders import WebBaseLoader, SeleniumURLLoader
from langchain.tools import Tool

def load_web_content(url: str) -> str:
    """
    Attempt to load webpage using WebBaseLoader; fallback to SeleniumURLLoader if needed.
    """
    try:
        # Try fast, simple HTML fetch
        print("[INFO] Trying WebBaseLoader...")
        loader = WebBaseLoader(url)
        docs = loader.load()
        if docs and docs[0].page_content.strip():
            return docs[0].page_content
    except Exception as e:
        print(f"[WARN] WebBaseLoader failed: {e}")

    try:
        # Fallback to JS-rendering scraper
        print("[INFO] Falling back to SeleniumURLLoader...")
        selenium_loader = SeleniumURLLoader(urls=[url])
        docs = selenium_loader.load()
        return docs[0].page_content if docs else "No content extracted."
    except Exception as e:
        print(f"[ERROR] SeleniumURLLoader also failed: {e}")
        return "Failed to load webpage content."

# Define the tool for Langchain agent
load_web_tool = Tool(
    name="WebPageContentLoader",
    func=load_web_content,
    description="Loads the full content of a webpage from a given URL. Tries standard loader first, falls back to Selenium for JavaScript-heavy pages."
)
