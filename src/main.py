from typin    def create_development_plan(self, project_description):
        # Conception Phase Tasks
        requirements_spec_task = self.tasks.create_requirements_specification_task(
            self.agents.product_owner,
            project_description
        )

        product_backlog_task = self.tasks.create_product_backlog_task(
            self.agents.product_owner,
            "{requirements_spec}"  # Will be replaced with actual requirements specification
        )

        mockups_task = self.tasks.create_mockups_task(
            self.agents.designer,
            "{requirements_spec}",  # Will be replaced with actual requirements specification
            "{product_backlog}"  # Will be replaced with actual product backlog
        )

        architecture_task = self.tasks.create_architecture_design_task(
            self.agents.developer,
            "{requirements_spec}",  # Will be replaced with actual requirements specification
            "{product_backlog}"  # Will be replaced with actual product backlog
        )

        # Implementation Phase Tasks
        development_task = self.tasks.create_development_task(
            self.agents.developer,
            "{mockups}",  # Will be replaced with actual mockups
            "{architecture}"  # Will be replaced with actual architecture design
        )m crewai import Crew, Task
from src.agents.agent_definitions import DevTeamAgents
from src.tasks.task_definitions import DevTeamTasks

class DevCrew:
    def __init__(self):
        self.agents = DevTeamAgents()
        self.tasks = DevTeamTasks()

    def create_development_plan(self, project_description):
        # Create tasks with dependencies
        requirements_task = self.tasks.create_product_requirements_task(
            self.agents.product_owner,
            project_description
        )

        design_task = self.tasks.create_design_task(
            self.agents.designer,
            "{requirements}"  # Will be replaced with actual requirements during execution
        )

        development_task = self.tasks.create_development_task(
            self.agents.developer,
            "{design_spec}",  # Will be replaced with actual design during execution
            "{requirements}"  # Will be replaced with actual requirements during execution
        )

        qa_task = self.tasks.create_qa_task(
            self.agents.qa_engineer,
            "{requirements}",  # Will be replaced with actual requirements during execution
            "{implementation}"  # Will be replaced with actual implementation during execution
        )

        devops_task = self.tasks.create_devops_task(
            self.agents.devops_engineer,
            "{implementation}"  # Will be replaced with actual implementation during execution
        )

        # Documentation tasks
        technical_docs_task = self.tasks.create_technical_documentation_task(
            self.agents.developer,
            "{requirements}",  # Will be replaced with actual requirements
            "{implementation}",  # Will be replaced with actual implementation
            "{design_spec}"  # Will be replaced with actual design spec
        )

        test_docs_task = self.tasks.create_test_documentation_task(
            self.agents.qa_engineer,
            "{test_plan}",  # Will be replaced with actual test plan
            "{test_results}"  # Will be replaced with actual test results
        )

        user_docs_task = self.tasks.create_user_documentation_task(
            self.agents.product_owner,
            "{requirements}",  # Will be replaced with actual requirements
            "{design_spec}",  # Will be replaced with actual design spec
            "{implementation}"  # Will be replaced with actual implementation
        )

        # Create the crew with ordered phases
        crew = Crew(
            agents=self.agents.get_all_agents(),
            tasks=[
                # Conception Phase
                requirements_spec_task,
                product_backlog_task,
                mockups_task,
                architecture_task,
                
                # Implementation Phase
                development_task,
                qa_task,
                devops_task,
                
                # Documentation Phase
                technical_docs_task,
                test_docs_task,
                user_docs_task
            ],
            verbose=True
        )

        # Start the crew's work
        result = crew.kickoff()
        return result

if __name__ == "__main__":
    # Example usage
    dev_crew = DevCrew()
    project_description = """
    Create a web application that allows users to:
    1. Upload and process images
    2. Apply various filters and effects
    3. Save and share processed images
    4. Manage their image library
    """
    
    result = dev_crew.create_development_plan(project_description)
    print(result)
