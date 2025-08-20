from crewai import Crew
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
            requirements_task
        )

        development_task = self.tasks.create_development_task(
            self.agents.developer,
            design_task,
            requirements_task
        )

        qa_task = self.tasks.create_qa_task(
            self.agents.qa_engineer,
            requirements_task,
            development_task
        )

        devops_task = self.tasks.create_devops_task(
            self.agents.devops_engineer,
            development_task
        )

        # Create the crew
        crew = Crew(
            agents=self.agents.get_all_agents(),
            tasks=[
                requirements_task,
                design_task,
                development_task,
                qa_task,
                devops_task
            ]
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
