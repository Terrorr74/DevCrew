from typing import List
from src.config.config import create_agent
from src.utils.tools import DevTeamTools

class DevTeamAgents:
    def __init__(self):
        self.developer = create_agent(
            role='Software Developer',
            goal='Design and implement high-quality code solutions based on user requirements',
            backstory="""You are a senior software developer with expertise in multiple programming 
            languages and frameworks. You specialize in:
            - Writing clean, efficient, and well-documented code
            - Understanding and implementing user requirements
            - Following best practices and design patterns
            - Using Context7 for accessing up-to-date documentation
            - Creating robust test cases
            - Code review and optimization
            - Error handling and input validation""",
            tools=DevTeamTools.get_developer_tools(),
            verbose=True
        )

        self.qa_engineer = create_agent(
            role='QA Engineer',
            goal='Ensure code quality and functionality through comprehensive testing',
            backstory="""You are a detail-oriented QA engineer with experience in various testing 
            methodologies. You excel at:
            - Writing and executing test cases
            - Identifying edge cases and potential issues
            - Validating input/output requirements
            - Ensuring code reliability and performance
            - Providing detailed feedback on code quality
            - Suggesting improvements and optimizations""",
            tools=DevTeamTools.get_qa_tools(),
            verbose=True
        )

    def get_all_agents(self) -> List:
        return [
            self.developer,
            self.qa_engineer
        ]
