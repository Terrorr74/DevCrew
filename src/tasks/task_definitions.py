from crewai import Task

class DevTeamTasks:
    @staticmethod
    def create_project_planning_task(agent, requirements_spec, product_backlog):
        return Task(
            description=f"""Create a comprehensive project plan based on:
            Requirements Specification: {requirements_spec}
            Product Backlog: {product_backlog}
            
            1. Define project timeline and milestones
            2. Create sprint planning and iterations
            3. Identify project risks and mitigation strategies
            4. Plan resource allocation and team capacity
            5. Define project KPIs and success metrics
            6. Create communication and reporting plan
            """,
            agent=agent,
            expected_output="""Provide a detailed project management plan including:
            - Project timeline with major milestones
            - Sprint schedule and velocity targets
            - Risk register with mitigation strategies
            - Resource allocation matrix
            - Project KPIs and metrics
            - Communication plan and stakeholder matrix
            - Dependencies and critical path analysis
            """
        )

    @staticmethod
    def create_sprint_planning_task(agent, product_backlog, project_plan):
        return Task(
            description=f"""Create detailed sprint plans based on:
            Product Backlog: {product_backlog}
            Project Plan: {project_plan}
            
            1. Define sprint goals and objectives
            2. Select and prioritize sprint backlog items
            3. Estimate story points and team capacity
            4. Identify sprint dependencies and risks
            5. Plan sprint ceremonies and meetings
            """,
            agent=agent,
            expected_output="""Provide sprint planning documentation including:
            - Sprint goals and objectives
            - Prioritized sprint backlog
            - Story point estimates and team capacity
            - Sprint dependencies and risk mitigation
            - Sprint ceremony schedule
            - Definition of Ready and Done
            """
        )

    @staticmethod
    def create_progress_tracking_task(agent, project_plan, sprint_plan):
        return Task(
            description=f"""Create progress tracking and reporting framework based on:
            Project Plan: {project_plan}
            Sprint Plan: {sprint_plan}
            
            1. Define progress tracking metrics
            2. Create burndown/burnup charts
            3. Set up progress reporting templates
            4. Define impediment tracking process
            5. Create sprint review template
            6. Define retrospective format
            7. Set up automated progress notifications
            8. Define sprint demo guidelines
            """,
            agent=agent,
            expected_output="""Provide progress tracking framework including:
            - Progress tracking metrics and KPIs
            - Burndown/burnup chart templates
            - Progress report templates
            - Impediment log format
            - Sprint review template
            - Retrospective format and guidelines
            - Status dashboard specification
            - Sprint demo presentation template
            - Daily progress notification format
            """
        )

    @staticmethod
    def create_git_workflow_task(agent, project_plan):
        return Task(
            description=f"""Create Git workflow and branching strategy based on:
            Project Plan: {project_plan}
            
            1. Define branching strategy (feature, develop, release, hotfix)
            2. Set up branch protection rules
            3. Define commit message conventions
            4. Create PR templates and guidelines
            5. Define release process
            6. Set up automated version tracking
            7. Define emergency hotfix procedures
            """,
            agent=agent,
            expected_output="""Provide comprehensive Git workflow documentation including:
            - Detailed branching strategy
            - Branch naming conventions
            - Commit message format
            - PR review checklist
            - Release process workflow
            - Version numbering scheme
            - Hotfix procedure
            - Deployment checklist
            """
        )

    @staticmethod
    def create_code_review_task(agent, feature_branch, requirements):
        return Task(
            description=f"""Perform comprehensive code review for:
            Feature Branch: {feature_branch}
            Requirements: {requirements}
            
            1. Review code quality and standards
            2. Check test coverage and quality
            3. Verify security best practices
            4. Review documentation completeness
            5. Check performance implications
            6. Verify requirement implementation
            7. Review error handling
            8. Check for technical debt
            """,
            agent=agent,
            expected_output="""Provide detailed code review report including:
            - Code quality assessment
            - Test coverage analysis
            - Security review findings
            - Documentation completeness check
            - Performance analysis
            - Requirements compliance check
            - Error handling review
            - Technical debt assessment
            - Recommendations for improvements
            """
        )

    @staticmethod
    def create_sprint_report_task(agent, sprint_data, progress_metrics):
        return Task(
            description=f"""Generate comprehensive sprint report based on:
            Sprint Data: {sprint_data}
            Progress Metrics: {progress_metrics}
            
            1. Summarize sprint achievements
            2. Report on completed user stories
            3. Analyze velocity and burndown
            4. List impediments and solutions
            5. Document technical decisions
            6. Report test coverage and quality
            7. Document customer feedback
            8. Provide next sprint recommendations
            """,
            agent=agent,
            expected_output="""Provide detailed sprint report including:
            - Sprint goals achievement status
            - Completed user stories and points
            - Velocity and burndown analysis
            - Impediments and resolutions
            - Technical decisions and rationale
            - Quality metrics and test coverage
            - Customer feedback summary
            - Recommendations for next sprint
            - Updated project timeline
            """
        )
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
