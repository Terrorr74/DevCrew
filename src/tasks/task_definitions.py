from crewai import Task

class DevTeamTasks:
    @staticmethod
    def create_requirements_specification_task(agent, project_description):
        return Task(
            description=f"""Create a detailed requirements specification document based on:
            Project Description: {project_description}
            
            1. Analyze project objectives and scope
            2. Define functional requirements
            3. Define non-functional requirements
            4. Define system constraints and limitations
            5. Define integration requirements
            6. Specify performance requirements
            7. Document security requirements
            """,
            agent=agent,
            expected_output="""Provide a comprehensive Software Requirements Specification (SRS) document including:
            - Executive Summary
            - Project Scope and Objectives
            - Detailed Functional Requirements
            - Non-functional Requirements
            - System Constraints and Dependencies
            - Performance Requirements
            - Security Requirements
            - Integration Requirements
            - Assumptions and Dependencies
            """
        )

    @staticmethod
    def create_product_backlog_task(agent, requirements_spec):
        return Task(
            description=f"""Create a prioritized product backlog based on:
            Requirements Specification: {requirements_spec}
            
            1. Break down requirements into user stories
            2. Prioritize user stories using MoSCoW method
            3. Define acceptance criteria for each story
            4. Estimate story complexity/effort
            5. Group stories into epics
            6. Define story dependencies
            """,
            agent=agent,
            expected_output="""Provide a structured product backlog including:
            - Prioritized list of user stories
            - Story priorities (Must have, Should have, Could have, Won't have)
            - Detailed acceptance criteria for each story
            - Story point estimates
            - Epic groupings
            - Dependencies map
            """
        )

    @staticmethod
    def create_mockups_task(agent, requirements_spec, product_backlog):
        return Task(
            description=f"""Create detailed mockups and prototypes based on:
            Requirements Specification: {requirements_spec}
            Product Backlog: {product_backlog}
            
            1. Design user interface mockups
            2. Create interactive prototypes
            3. Design user flows and interactions
            4. Create responsive design specifications
            5. Define animation and transition specs
            """,
            agent=agent,
            expected_output="""Provide comprehensive design deliverables including:
            - UI mockups for all major screens
            - Interactive prototype specifications
            - User flow diagrams
            - Responsive design guidelines
            - Animation and transition specifications
            - Design system documentation
            """
        )

    @staticmethod
    def create_architecture_design_task(agent, requirements_spec, product_backlog):
        return Task(
            description=f"""Create detailed architecture diagrams and documentation based on:
            Requirements Specification: {requirements_spec}
            Product Backlog: {product_backlog}
            
            1. Design system architecture
            2. Create component diagrams
            3. Define data models and relationships
            4. Specify API architectures
            5. Design deployment architecture
            6. Define security architecture
            """,
            agent=agent,
            expected_output="""Provide comprehensive architecture documentation including:
            - High-level system architecture diagram
            - Component interaction diagrams
            - Data model diagrams and specifications
            - API architecture documentation
            - Deployment architecture diagram
            - Security architecture specification
            - Technology stack specification
            - Integration points documentation
            """
        )

    @staticmethod
    def create_technical_documentation_task(agent, requirements, implementation, design_spec):
        return Task(
            description=f"""Create comprehensive technical documentation based on:
            Requirements: {requirements}
            Implementation: {implementation}
            Design Spec: {design_spec}
            
            1. Create system architecture documentation
            2. Document API specifications
            3. Create code documentation guidelines
            4. Document development setup instructions
            5. Create maintenance and troubleshooting guides
            """,
            agent=agent,
            expected_output="""Provide complete technical documentation including:
            - System architecture overview and diagrams
            - API documentation with endpoints, requests, and responses
            - Code documentation standards
            - Development environment setup guide
            - Maintenance procedures and troubleshooting guides
            """
        )

    @staticmethod
    def create_test_documentation_task(agent, test_plan, test_results):
        return Task(
            description=f"""Create test documentation based on:
            Test Plan: {test_plan}
            Test Results: {test_results}
            
            1. Document test strategies and methodologies
            2. Create test case documentation
            3. Document test results and coverage
            4. Create test environment setup guides
            5. Document bug reporting procedures
            """,
            agent=agent,
            expected_output="""Provide comprehensive test documentation including:
            - Detailed test strategies and methodologies
            - Test case documentation with scenarios
            - Test results analysis and metrics
            - Test environment setup instructions
            - Bug reporting and tracking procedures
            """
        )

    @staticmethod
    def create_user_documentation_task(agent, requirements, design_spec, implementation):
        return Task(
            description=f"""Create user documentation based on:
            Requirements: {requirements}
            Design Spec: {design_spec}
            Implementation: {implementation}
            
            1. Create user manuals and guides
            2. Document feature usage instructions
            3. Create troubleshooting guides for users
            4. Document FAQs and common issues
            5. Create quick-start guides
            """,
            agent=agent,
            expected_output="""Provide complete user documentation including:
            - Comprehensive user manual
            - Feature-specific guides and tutorials
            - User troubleshooting guide
            - FAQ document
            - Quick-start guide for new users
            """
        )
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
