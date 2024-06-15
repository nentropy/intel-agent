from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain import hub

cot_step1 = hub.pull("rachnogstyle/nlw_jan24_cot_step1")
cot_step2 = hub.pull("rachnogstyle/nlw_jan24_cot_step2")
cot_step3 = hub.pull("rachnogstyle/nlw_jan24_cot_step3")
cot_step4 = hub.pull("rachnogstyle/nlw_jan24_cot_step4")

model = "gpt-4o"

chain1 = LLMChain(
    llm=ChatOpenAI(temperature=0, model=model),
    prompt=cot_step1,
    output_key="solutions"
)

chain2 = LLMChain(
    llm=ChatOpenAI(temperature=0, model=model),
    prompt=cot_step2,
    output_key="review"
)

chain3 = LLMChain(
    llm=ChatOpenAI(temperature=0, model=model),
    prompt=cot_step3,
    output_key="deepen_thought_process"
)

chain4 = LLMChain(
    llm=ChatOpenAI(temperature=0, model=model),
    prompt=cot_step4,
    output_key="ranked_solutions"
)

