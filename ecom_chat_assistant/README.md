# Assistant Product Information Extractor
### Overview

This project demonstrates how to use an LLM (Large Language Model) with Pydantic for structured output.
The assistant is designed to take product-related information from user prompts and convert it into a validated schema using Pydantic models.

The extracted details include:

Product Name (string)
Product Details (string)
Tentative Price (in USD, represented as int or float)

Additionally, a ChatPromptTemplate is used to guide the assistant in consistently extracting and formatting the required product information.