from typing import List
from src.config.config import create_agent
from src.utils.tools import DevTeamTools

class DevTeamAgents:
    def __init__(self):
        self.documentation_specialist = create_agent(
            role='Documentation Specialist',
            goal='Create comprehensive and clear documentation for all aspects of the project',
            backstory="""You are an experienced technical writer and documentation specialist with 
            expertise in creating user guides, API documentation, and technical specifications. 
            You excel at making complex information accessible and maintaining documentation quality.""",
            tools=DevTeamTools.get_documentation_tools(),
            verbose=True
        )

        self.product_owner = create_agent(
            role='Product Owner & Project Manager',
            goal='Define product vision, manage project execution, and ensure value delivery',
            backstory="""You are an experienced Product Owner and Project Manager with a strong background in 
            agile methodologies and software development. You excel at understanding user needs,
            defining requirements, and ensuring the product delivers value. You are also skilled in:
            - Project planning and execution
            - Sprint planning and management
            - Risk assessment and mitigation
            - Resource allocation and timeline management
            - Stakeholder communication
            - Agile ceremonies facilitation
            - Project metrics and KPI tracking""",
            tools=DevTeamTools.get_product_owner_tools(),
            verbose=True,
            allow_delegation=True
        )

        self.developer = create_agent(
            role='Software Developer & Version Control Manager',
            goal='Implement high-quality, maintainable code and manage version control workflow',
            backstory="""You are a senior software developer with expertise in multiple programming 
            languages and frameworks. You focus on writing clean, efficient code and following 
            best practices in software development. You are also an expert in:
            - Git workflow management
            - Feature branch development
            - Code review processes
            - Version control best practices
            - Release management
            - Continuous Integration practices
            - Technical documentation
            - Code quality monitoring""",
            tools=DevTeamTools.get_developer_tools(),
            verbose=True
        )

        self.qa_engineer = create_agent(
            role='QA Engineer',
            goal='Ensure software quality through comprehensive testing',
            backstory="""You are a detail-oriented QA engineer with experience in various testing 
            methodologies. You excel at finding edge cases and ensuring software reliability.""",
            tools=DevTeamTools.get_qa_tools(),
            verbose=True
        )

        self.designer = create_agent(
            role='UI/UX Designer',
            goal='Create intuitive and appealing user interfaces and experiences',
            backstory="""You are a creative UI/UX designer with a strong understanding of user-centered 
            design principles. You create designs that are both beautiful and functional.""",
            tools=DevTeamTools.get_architect_tools(),  # Using architect tools for design documentation
            verbose=True
        )

        self.devops_engineer = create_agent(
            role='DevOps Engineer',
            goal='Optimize development operations and ensure reliable deployment',
            backstory="""You are a DevOps engineer skilled in automation, CI/CD, and cloud technologies. 
            You ensure smooth deployment and operation of software systems.""",
            tools=DevTeamTools.get_devops_tools(),
            verbose=True
        )

    def get_all_agents(self) -> List:
        return [
            self.product_owner,
            self.developer,
            self.qa_engineer,
            self.designer,
            self.devops_engineer,
            self.documentation_specialist
        ]
