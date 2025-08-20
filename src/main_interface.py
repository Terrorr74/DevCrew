"""Main interface for AI Development Teams."""
from typing import Dict, Any, Optional
from crewai import Crew
from rich.console import Console
from rich.prompt import Prompt, Confirm

from src.agents.agent_definitions import DevTeamAgents, ProjectTeamAgents
from src.tasks.task_definitions import DevTeamTasks

console = Console()

class AIDevelopmentInterface:
    """Interface for interacting with AI development teams."""
    
    def __init__(self):
        self.dev_team = DevTeamAgents()
        self.project_team = ProjectTeamAgents()
        self.tasks = DevTeamTasks()

    def get_user_choice(self) -> str:
        """Get the user's choice of action."""
        console.print("\n[bold blue]Welcome to the AI Development Teams Interface![/bold blue]")
        console.print("\n[yellow]What would you like to do?[/yellow]")
        
        choice = Prompt.ask(
            "Choose an option",
            choices=[
                "1. Generate a script or program",
                "2. Plan a complete project",
                "3. Exit"
            ]
        )
        
        return choice.split(".")[0]  # Return just the number

    def generate_script(self) -> Optional[str]:
        """Handle script generation using the development team."""
        console.print("\n[bold green]Script Generation Mode[/bold green]")
        
        # Get script requirements
        script_type = Prompt.ask(
            "Choose script type",
            choices=[
                "Data Processing",
                "Web Scraping",
                "API Integration",
                "File Management",
                "Database Operations",
                "Automation Task",
                "Custom Script"
            ]
        )

        language = Prompt.ask(
            "Choose programming language",
            choices=[
                "Python",
                "JavaScript",
                "TypeScript",
                "Ruby",
                "Go",
                "Other"
            ]
        )

        console.print("\n[yellow]Please describe what your script should do:[/yellow]")
        description = input("> ")

        requirements = {
            "script_type": script_type,
            "language": language,
            "description": description
        }

        # Create and run the development crew
        development_task = self.tasks.create_development_task(
            agent=self.dev_team.developer,
            design_spec=f"Create a {language} script for {script_type}",
            requirements=description
        )

        testing_task = self.tasks.create_qa_task(
            agent=self.dev_team.qa_engineer,
            requirements=description,
            implementation="[AWAIT DEVELOPMENT TASK]"
        )

        crew = Crew(
            agents=[
                self.dev_team.developer,
                self.dev_team.qa_engineer
            ],
            tasks=[
                development_task,
                testing_task
            ]
        )

        try:
            result = crew.kickoff()
            return str(result)
        except Exception as e:
            console.print(f"[red]Error during script generation: {str(e)}[/red]")
            return None

    def plan_project(self) -> Optional[str]:
        """Handle complete project planning using both teams."""
        console.print("\n[bold green]Project Planning Mode[/bold green]")
        
        console.print("\n[yellow]Please describe your project:[/yellow]")
        description = input("> ")

        # Create tasks for the planning phase
        requirements_task = self.tasks.create_requirements_specification_task(
            self.project_team.product_owner,
            description
        )

        backlog_task = self.tasks.create_product_backlog_task(
            self.project_team.product_owner,
            "[AWAIT REQUIREMENTS]"
        )

        architecture_task = self.tasks.create_architecture_design_task(
            self.project_team.architect,
            "[AWAIT REQUIREMENTS]",
            "[AWAIT BACKLOG]"
        )

        # Create implementation tasks
        development_task = self.tasks.create_development_task(
            self.dev_team.developer,
            "[AWAIT ARCHITECTURE]",
            "[AWAIT REQUIREMENTS]"
        )

        testing_task = self.tasks.create_qa_task(
            self.dev_team.qa_engineer,
            "[AWAIT REQUIREMENTS]",
            "[AWAIT DEVELOPMENT]"
        )

        devops_task = self.tasks.create_devops_task(
            self.project_team.devops_engineer,
            "[AWAIT ARCHITECTURE]"
        )

        docs_task = self.tasks.create_technical_documentation_task(
            self.project_team.documentation_specialist,
            "[AWAIT REQUIREMENTS]",
            "[AWAIT DEVELOPMENT]",
            "[AWAIT ARCHITECTURE]"
        )

        # Create and run the full project crew
        crew = Crew(
            agents=[
                self.project_team.product_owner,
                self.project_team.architect,
                self.dev_team.developer,
                self.dev_team.qa_engineer,
                self.project_team.devops_engineer,
                self.project_team.documentation_specialist
            ],
            tasks=[
                requirements_task,
                backlog_task,
                architecture_task,
                development_task,
                testing_task,
                devops_task,
                docs_task
            ]
        )

        try:
            result = crew.kickoff()
            return str(result)
        except Exception as e:
            console.print(f"[red]Error during project planning: {str(e)}[/red]")
            return None

    def run(self):
        """Main interface loop."""
        while True:
            choice = self.get_user_choice()
            
            if choice == "1":
                result = self.generate_script()
                if result:
                    console.print("\n[bold green]Script Generation Complete![/bold green]")
                    console.print(result)
            
            elif choice == "2":
                result = self.plan_project()
                if result:
                    console.print("\n[bold green]Project Planning Complete![/bold green]")
                    console.print(result)
            
            elif choice == "3":
                console.print("\n[yellow]Thank you for using the AI Development Teams![/yellow]")
                break

            # Ask if user wants to continue
            if not Confirm.ask("\nWould you like to perform another task?"):
                console.print("\n[yellow]Thank you for using the AI Development Teams![/yellow]")
                break

def main():
    interface = AIDevelopmentInterface()
    interface.run()

if __name__ == "__main__":
    main()
