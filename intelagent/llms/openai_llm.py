import os
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


MODEL="gpt4o" 

def create_oai_llm(temp=0.0, max_tokens=2000):
    return ChatOpenAI(key=os.getenv("OPENAI_API_KEY"), model=MODEL, temperature=temp, max_tokens=max_tokens)
    
def create_oai_embedder():
    return OpenAIEmbeddings(model="text-embedding-small") #@TODO FIX