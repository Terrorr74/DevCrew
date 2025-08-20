from config.config import create_agent
from crewai import Task, Crew

# Create a test researcher agent
researcher = create_agent(
    role="Research Analyst",
    goal="Analyze and summarize information effectively",
    backstory="You are an experienced research analyst with expertise in gathering and summarizing information."
)

# Create a simple test task
research_task = Task(
    description="Provide a brief summary of the current state of AI technology.",
    expected_output="A concise overview of current AI technology trends and developments.",
    agent=researcher
)

# Create a crew with just this agent and task
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)

# Run the crew and get the result
result = crew.kickoff()

print("\n=== Test Result ===")
print(result)
