from pydantic import BaseModel
from typing import Union
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import PydanticOutputParser

#Pydantic model
class Product(BaseModel):
    product_name: str
    product_details: str
    tentative_price_usd: Union[int, float]
# 2. Create a Pydantic parser
parser = PydanticOutputParser(pydantic_object=Product)

#load env variables
load_dotenv()
os.getenv("LANGCHAIN_PROJECT")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]="true"


llm_response=ChatGroq(model="qwen/qwen3-32b")

# 3. Create a ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that extracts product name, product details and tentative price in $ ."),
    ("user", "Extract product information from this description:\n{product_description}\n\n"
             "Format your response as JSON.\n\n{format_instructions}")
])


# 5. Format prompt with parser instructions
final_prompt = prompt.format_messages(
    product_description="iPhone",
    format_instructions=parser.get_format_instructions()
)

# 6. Run through LLM
response = llm_response.invoke(final_prompt)

# 7. Parse response into Pydantic model
product = parser.parse(response.content)

print(product)