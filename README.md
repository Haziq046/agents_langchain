# AI Assistant with Web Search Capabilities

This project implements an AI assistant with web search capabilities using Streamlit, LangChain, and OpenAI's GPT model.

## Features

- Interactive chat interface
- Web search integration using DuckDuckGo
- Powered by OpenAI's GPT-4 model

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/agents_langchain.git
   ```

2. Install the required dependencies:
   ```
   pip install streamlit langchain langchain-openai langchain-community openai duckduckgo-search
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.streamlit/secrets.toml` file in the project root
   - Add your OpenAI API key to the file:
     ```
     OPENAI_API_KEY = "your-api-key-here"
     ```

## Usage

Run the Streamlit app:
