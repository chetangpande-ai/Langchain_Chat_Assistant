import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_groq import ChatGroq


load_dotenv()
os.getenv("LANGCHAIN_PROJECT")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

os.environ["LANGCHAIN_TRACING_V2"]="true"

llm=ChatGroq(model="qwen/qwen3-32b")
response=llm.invoke("what are the steps to balance the checmaical equation in acedic medium(redox reaction)")
print(response.content)

from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate=(
[
    ("system","You are an expert AI Engineer. Provide me answer based on the question"),
    ("user","{input}")
]
)
prompt


response=ChatGroq(model="qwen/qwen3-32b")

chain=prompt|response
chain