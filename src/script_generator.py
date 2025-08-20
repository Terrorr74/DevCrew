"""Script generator using AI development team."""
from typing import Dict, Any
from crewai import Crew
from rich.console import Console
from rich.prompt import Prompt, Confirm

from src.agents.agent_definitions import DevTeamAgents
from src.tasks.task_definitions import DevTeamTasks

console = Console()

class ScriptGenerator:
    def __init__(self):
        self.agents = DevTeamAgents()
        self.tasks = DevTeamTasks()

    def get_user_requirements(self) -> Dict[str, Any]:
        """Get script requirements from the user."""
        console.print("\n[bold blue]Welcome to the AI Script Generator![/bold blue]")
        
        # Get script type
        console.print("\n[yellow]What type of script would you like to create?[/yellow]")
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

        # Get programming language
        console.print("\n[yellow]Which programming language would you like to use?[/yellow]")
        language = Prompt.ask(
            "Choose language",
            choices=[
                "Python",
                "JavaScript",
                "TypeScript",
                "Ruby",
                "Go",
                "Other"
            ]
        )

        # Get script description
        console.print("\n[yellow]Please describe what your script should do:[/yellow]")
        description = input("> ")

        # Get additional requirements
        has_additional = Confirm.ask("\nWould you like to add any additional requirements?")
        additional_reqs = ""
        if has_additional:
            console.print("[yellow]Please enter additional requirements:[/yellow]")
            additional_reqs = input("> ")

        return {
            "script_type": script_type,
            "language": language,
            "description": description,
            "additional_requirements": additional_reqs
        }

    def generate_script(self, requirements: Dict[str, Any]) -> str:
        """Generate the script using the AI development team."""
        # Create script specifications
        script_spec = f"""Design specification for {requirements['language']} script:
            Type: {requirements['script_type']}
            Requirements: {requirements['description']}
            Additional Requirements: {requirements['additional_requirements']}
            
            The implementation should:
            1. Follow {requirements['language']} best practices
            2. Include proper error handling
            3. Include input validation
            4. Be well-documented
            5. Be efficiently structured"""
            
        # Create development task
        development_task = self.tasks.create_development_task(
            agent=self.agents.developer,
            design_spec=script_spec,
            requirements=requirements['description']
        )

        # Create testing task with implementation results
        testing_task = self.tasks.create_qa_task(
            agent=self.agents.qa_engineer,
            requirements=requirements['description'],
            implementation="[AWAIT DEVELOPMENT TASK RESULT]"
        )

        # Create and run the crew
        crew = Crew(
            agents=[self.agents.developer, self.agents.qa_engineer],
            tasks=[development_task, testing_task]
        )

        try:
            result = crew.kickoff()
            return str(result)  # Convert CrewOutput to string
        except Exception as e:
            return f"Error during script generation: {str(e)}"

def main():
    generator = ScriptGenerator()
    
    try:
        # Get requirements from user
        requirements = generator.get_user_requirements()
        
        # Generate the script
        console.print("\n[bold green]Generating script...[/bold green]")
        result = generator.generate_script(requirements)
        
        # Display results
        console.print("\n[bold green]Script Generation Complete![/bold green]")
        console.print(result)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Script generation cancelled by user.[/yellow]")
    except Exception as e:
        console.print(f"\n[red]Error during script generation: {str(e)}[/red]")

if __name__ == "__main__":
    main()
