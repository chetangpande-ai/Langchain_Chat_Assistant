import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
os.getenv("LANGCHAIN_PROJECT")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]="true"

prompt=ChatPromptTemplate.from_messages(
[
    ("system","You are an expert AI Engineer. Provide me answer based on the question"),
    ("user","{input}")
]
)
prompt

llm_response=ChatGroq(model="qwen/qwen3-32b")
chain=prompt|llm_response
chain

response=chain.invoke({"input":"Can you tell me something about Langsmith"})
print(response.content)