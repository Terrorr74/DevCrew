from crewai import Task

class DevTeamTasks:
    @staticmethod
    def create_product_requirements_task(agent, project_description):
        return Task(
            description=f"""Analyze the following project and create detailed requirements:
            {project_description}
            
            1. Define the core features and functionality
            2. Prioritize requirements
            3. Create user stories
            4. Define acceptance criteria
            """,
            agent=agent,
            expected_output="""Provide a detailed document containing:
            - List of core features with priorities
            - User stories in standard format
            - Acceptance criteria for each feature
            - Dependencies and constraints
            """
        )

    @staticmethod
    def create_design_task(agent, requirements):
        return Task(
            description=f"""Based on these requirements, create a design specification:
            {requirements}
            
            1. Create UI/UX design guidelines
            2. Define component specifications
            3. Create wireframes description
            4. Define user interactions
            """,
            agent=agent,
            expected_output="""Provide a comprehensive design document including:
            - UI/UX guidelines (colors, typography, spacing)
            - Component specifications with descriptions
            - Wireframe descriptions for each major screen
            - User interaction flows and behaviors
            """
        )

    @staticmethod
    def create_development_task(agent, design_spec, requirements):
        return Task(
            description=f"""Implement the solution based on:
            Requirements: {requirements}
            Design Spec: {design_spec}
            
            1. Plan the technical architecture
            2. Write code implementation steps
            3. Define code structure
            4. List potential technical challenges
            """,
            agent=agent,
            expected_output="""Provide a technical implementation plan including:
            - Detailed architecture design
            - Technology stack specifications
            - Code structure and organization
            - Implementation steps and timeline
            - Identified technical challenges and solutions
            """
        )

    @staticmethod
    def create_qa_task(agent, requirements, implementation):
        return Task(
            description=f"""Create a testing strategy for:
            Requirements: {requirements}
            Implementation: {implementation}
            
            1. Define test scenarios
            2. Create test cases
            3. Plan integration tests
            4. Define acceptance testing criteria
            """,
            agent=agent,
            expected_output="""Provide a comprehensive testing plan including:
            - Test scenarios and test cases
            - Integration testing approach
            - Acceptance testing criteria
            - Testing timeline and resources needed
            - Quality metrics and benchmarks
            """
        )

    @staticmethod
    def create_devops_task(agent, implementation):
        return Task(
            description=f"""Create deployment and operations plan for:
            Implementation: {implementation}
            
            1. Define deployment strategy
            2. Create CI/CD pipeline plan
            3. Define monitoring strategy
            4. Plan scaling approach
            """,
            agent=agent,
            expected_output="""Provide a complete DevOps strategy including:
            - Deployment pipeline architecture
            - CI/CD workflow specifications
            - Monitoring and alerting setup
            - Scaling strategy and infrastructure requirements
            - Security and backup procedures
            """
        )
