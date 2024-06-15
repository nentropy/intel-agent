from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from tools.memory import retriever_tool

search = TavilySearchAPIWrapper()
tavily_tool = TavilySearchResults(api_wrapper=search)

llm = ChatOpenAI(model_name="gpt-4o", temperature=0.0)
agent_chain = initialize_agent(
    [retriever_tool, tavily_tool],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
