import os
from dotenv import load_dotenv
import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY") or st.secrets["openai"]["api_key"]
if not openai_api_key:
    st.error("OpenAI API key not found. Please set it in your .env file or Streamlit secrets.")
    st.stop()

# Set the API key in the environment
os.environ["OPENAI_API_KEY"] = openai_api_key

# Initialize the language model with the correct model name
llm = ChatOpenAI(temperature=0, model="gpt-4")

# Initialize the search tool
search = DuckDuckGoSearchRun()

# Initialize the agent
agent = initialize_agent(
    [search],
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

# Streamlit UI
st.title("AI Assistant with Web Search Capabilities")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What would you like to know?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = agent.run(prompt)
        st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
