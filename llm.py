from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def llm():
    gemini_ll=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",
            temperature=0.8)
    
    return gemini_ll