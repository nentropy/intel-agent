from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from llms.cohere_llm import create_cohere_llm
from llms.openai_llm import create_oai_llm

#@TODO ADD ERROR HANDLING

search = TavilySearchAPIWrapper()
tavily_tool = TavilySearchResults(api_wrapper=search)

try:
    llm = create_cohere_llm()
except Exception as e:
    llm = create_oai_llm()
    #_logger.error(e, exc_info=True)

agent_chain = initialize_agent(
    [tavily_tool],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True)

agent_chain.run(
    "What are the Neurons Lab services",
)



