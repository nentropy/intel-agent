from cohere_llm import create_cohere_llm
from openai_llm import create_oai_llm

PROVIDER = "OPENAI" # COHERE, OPENAI
MODEL=""

if PROVIDER == "OPENAI":
    MODEL == create_oai_llm()
elif PROVIDER == "COHERE":
    MODEL == create_cohere_llm()