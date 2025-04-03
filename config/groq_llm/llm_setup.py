from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

# Initialize the chat model globally so it's reused across calls
llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")
