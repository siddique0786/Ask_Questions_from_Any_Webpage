from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI  # Placeholder for Gemini
from tools.webpage_loader import load_web_tool
from llm import llm

# Replace with Gemini integration when officially available in Langchain
def create_agent():
    # llm = ChatOpenAI(temperature=0, model="gpt-4")  # Placeholder
    tools = [load_web_tool]

    agent = initialize_agent(
        tools=tools,
        llm=llm(),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    return agent
