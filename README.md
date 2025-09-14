### create venv and activate
```
conda create -p venv python=3.12
conda activate ./venv
```


### Pydantic
Pydantic is a Python library for data validation and parsing using Python type hints. It automatically validates input data against defined models and provides clear error messages for invalid data.

Pydantic BaseModel allows configuration through a Config class and Field() functions. Common options include validate_assignment=True for runtime validation, extra="forbid" to reject unknown fields, and field constraints like min_length, regex for validation rules.

```
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: Optional[int] = None    # Optional with None default
    email: str = "default@example.com"  # Optional with default value

```

# Langchain 


## Companies and LLM Models
```
Google- Gemini
Meta-Lama
AWS-Cloud
Anthropic-Claude
OpenAI-GPT
Microsfot-Cloud
Grok-Grok
```