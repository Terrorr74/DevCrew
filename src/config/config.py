import os
from typing import List, Optional, Sequence, Any
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from crewai import Agent
from crewai.tools import BaseTool

# Load environment variables
load_dotenv()

# Initialize the LLM for CrewAI
llm = OllamaLLM(
    model="llama2",  # Using Llama 2 model
    base_url="http://localhost:11434",
    temperature=0.7,
    num_ctx=4096,  # Context window size
    num_thread=4   # Number of threads for processing
)

def create_agent(
    role: str,
    goal: str,
    backstory: str,
    tools: Optional[Sequence[BaseTool]] = None,
    verbose: bool = True,
    allow_delegation: bool = False
) -> Agent:
    """
    Create an agent with the configured LLM and optional tools
    
    Args:
        role: The role of the agent
        goal: The agent's goal
        backstory: The agent's backstory
        tools: Optional sequence of tools for the agent
        verbose: Whether to enable verbose output
        allow_delegation: Whether to allow task delegation
    
    Returns:
        Agent: Configured agent with the specified tools
    """
    tool_list: List[BaseTool] = list(tools) if tools is not None else []
    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        tools=tool_list,
        verbose=verbose,
        allow_delegation=allow_delegation,
        llm=llm
    )
