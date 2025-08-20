from typing import List, Sequence
from crewai import Crew, Task
from src.agents.agent_definitions import DevTeamAgents
from src.tasks.task_definitions import DevTeamTasks

class DevCrew:
    def __init__(self):
        self.agents = DevTeamAgents()
        self.tasks = DevTeamTasks()

    def create_development_plan(self, project_description: str) -> str:
        """
        Creates a complete development plan going through conception, implementation, and documentation phases.
        
        Args:
            project_description: Initial project requirements and description
            
        Returns:
            str: The complete development plan with all phases' outputs
        """
        # Conception Phase
        requirements_spec_task = self.tasks.create_requirements_specification_task(
            self.agents.product_owner,
            project_description
        )

        product_backlog_task = self.tasks.create_product_backlog_task(
            self.agents.product_owner,
            "[PREV_TASK_RESULT]"  # Will be replaced with requirements_spec_task result
        )

        mockups_task = self.tasks.create_mockups_task(
            self.agents.designer,
            "[PREV_TASK_RESULT]",  # Will be replaced with requirements_spec_task result
            "[PREV_TASK_RESULT]"   # Will be replaced with product_backlog_task result
        )

        architecture_task = self.tasks.create_architecture_design_task(
            self.agents.developer,
            "[PREV_TASK_RESULT]",  # Will be replaced with requirements_spec_task result
            "[PREV_TASK_RESULT]"   # Will be replaced with product_backlog_task result
        )

        # Implementation Phase
        development_task = self.tasks.create_development_task(
            self.agents.developer,
            "[PREV_TASK_RESULT]",  # Will be replaced with mockups_task result
            "[PREV_TASK_RESULT]"   # Will be replaced with architecture_task result
        )

        qa_task = self.tasks.create_qa_task(
            self.agents.qa_engineer,
            "[PREV_TASK_RESULT]",  # Will be replaced with requirements_spec_task result
            "[PREV_TASK_RESULT]"   # Will be replaced with development_task result
        )

        devops_task = self.tasks.create_devops_task(
            self.agents.devops_engineer,
            "[PREV_TASK_RESULT]"   # Will be replaced with development_task result
        )

        # Documentation Phase
        technical_docs_task = self.tasks.create_technical_documentation_task(
            self.agents.documentation_specialist,
            "[PREV_TASK_RESULT]",  # Will be replaced with requirements_spec_task result
            "[PREV_TASK_RESULT]",  # Will be replaced with development_task result
            "[PREV_TASK_RESULT]"   # Will be replaced with architecture_task result
        )

        test_docs_task = self.tasks.create_test_documentation_task(
            self.agents.documentation_specialist,
            "[PREV_TASK_RESULT]",  # Will be replaced with qa_task plan result
            "[PREV_TASK_RESULT]"   # Will be replaced with qa_task results
        )

        user_docs_task = self.tasks.create_user_documentation_task(
            self.agents.documentation_specialist,
            "[PREV_TASK_RESULT]",  # Will be replaced with requirements_spec_task result
            "[PREV_TASK_RESULT]",  # Will be replaced with mockups_task result
            "[PREV_TASK_RESULT]"   # Will be replaced with development_task result
        )

        # Configure task dependencies
        product_backlog_task.context = [requirements_spec_task]
        mockups_task.context = [requirements_spec_task, product_backlog_task]
        architecture_task.context = [requirements_spec_task, product_backlog_task]
        development_task.context = [mockups_task, architecture_task]
        qa_task.context = [requirements_spec_task, development_task]
        devops_task.context = [development_task]
        technical_docs_task.context = [requirements_spec_task, development_task, architecture_task]
        test_docs_task.context = [qa_task]
        user_docs_task.context = [requirements_spec_task, mockups_task, development_task]

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
