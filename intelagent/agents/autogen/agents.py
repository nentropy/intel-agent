"""
BASE AGENTS
===========


"""
MODEL="gpt4o"

import autogen
from autogen import AssistantAgent, UserProxyAgent

llm_config = {"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]