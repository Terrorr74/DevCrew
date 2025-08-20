import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from crewai import Agent

# Load environment variables
load_dotenv()

# Initialize the LLM for CrewAI
llm = OllamaLLM(
    model="ollama/mistral:latest",  # Include the provider prefix
    base_url="http://localhost:11434",
    temperature=0.7
)

def create_agent(
    role: str,
    goal: str,
    backstory: str,
    verbose: bool = True,
    allow_delegation: bool = False
) -> Agent:
    """
    Create an agent with the configured LLM
    """
    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        verbose=verbose,
        allow_delegation=allow_delegation,
        llm=llm
    )
