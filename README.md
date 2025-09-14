# LangChain Groq AI Application

A simple AI application using LangChain with Groq's language models, featuring LangSmith tracing for monitoring and debugging.

## Features

- 🤖 AI-powered question answering using Groq's language models
- 📊 LangSmith integration for tracing and monitoring
- 🔧 Environment-based configuration
- 🚀 Simple chain-based architecture

## Prerequisites

- Python 3.8+
- Groq API key
- LangChain API key (for tracing)

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Install dependencies**
   ```bash
   pip install langchain-groq python-dotenv langchain-core
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   LANGCHAIN_API_KEY=your_langchain_api_key_here
   OPENAI_API_KEY=your_openai_key_here
   LANGCHAIN_PROJECT=AgenticApplication
   LANGCHAIN_TRACING_V2=true
   ```

## Getting API Keys

### Groq API Key
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up/Login
3. Navigate to API Keys section
4. Generate new API key

### LangChain API Key
1. Visit [smith.langchain.com](https://smith.langchain.com)
2. Sign up/Login
3. Go to Settings > API Keys
4. Create new API key

## Usage

Run the application:
```bash
python main.py
```

The application will:
1. Load environment variables
2. Initialize the Groq language model
3. Set up a prompt template for AI engineering questions
4. Process your input and return an AI response
5. Trace the execution in LangSmith

## Code Structure

```python
# Environment setup and API key configuration
load_dotenv()

# Prompt template for AI engineering questions
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert AI Engineer. Provide me answer based on the question"),
    ("user", "{input}")
])

# Language model initialization
llm_response = ChatGroq(model="qwen/qwen3-32b")

# Output parsing for clean string responses
output_parser = StrOutputParser()

# Chain creation: prompt → model → parser
chain = prompt | llm_response | output_parser
```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key | ✅ |
| `LANGCHAIN_API_KEY` | LangChain API key for tracing | ✅ |
| `OPENAI_API_KEY` | OpenAI API key (if needed) | ⚠️ |
| `LANGCHAIN_PROJECT` | Project name for LangSmith | ✅ |
| `LANGCHAIN_TRACING_V2` | Enable tracing | ✅ |

### Available Models

The application uses Groq's models. Popular options:
- `llama3-8b-8192`
- `llama3-70b-8192`
- `mixtral-8x7b-32768`
- `gemma-7b-it`

## Monitoring

This application integrates with LangSmith for:
- 📈 Performance monitoring
- 🔍 Request/response tracing
- 🐛 Debugging support
- 📊 Usage analytics

View your traces at [smith.langchain.com](https://smith.langchain.com)

## Example Output

```
Input: "Can you tell me something about Langsmith"

Output: LangSmith is a platform developed by LangChain for monitoring, 
debugging, and improving LLM applications. It provides comprehensive 
tracing capabilities, performance analytics, and helps developers 
optimize their AI workflows...
```

## Troubleshooting

### Common Issues

1. **Missing API Keys**
   - Ensure all required environment variables are set in `.env`
   - Check API key validity

2. **Model Not Found**
   - Verify the model name exists in Groq's catalog
   - Try using `llama3-8b-8192` as a fallback

3. **Tracing Not Working**
   - Confirm `LANGCHAIN_TRACING_V2=true`
   - Verify LangChain API key is valid
   - Check project name in LangSmith dashboard

### Debug Commands

```bash
# Check environment variables
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('GROQ_API_KEY'))"

# Test API connection
python -c "from langchain_groq import ChatGroq; llm = ChatGroq(model='llama3-8b-8192'); print('Connection successful')"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
- 📧 Create an issue in this repository
- 📖 Check [LangChain documentation](https://docs.langchain.com)
- 🔗 Visit [Groq documentation](https://console.groq.com/docs)