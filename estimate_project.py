from typing import Dict, List, Tuple
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from src.utils.progress_tracker import ProgressManager
from src.main import DevCrew
import time

console = Console()

class ProjectEstimator:
    """
    Handles project time estimation with configurable complexity factors
    """
    
    # Base time estimates in minutes for each phase
    BASE_PHASE_TIMES = {
        "Requirements Analysis": 30,
        "Product Backlog Creation": 45,
        "System Architecture Design": 60,
        "UI/UX Design": 45,
        "Development Planning": 60,
        "QA Strategy": 30,
        "DevOps Setup": 45,
        "Technical Documentation": 30,
        "User Documentation": 30
    }
    
    # Complexity multipliers for different project sizes
    COMPLEXITY_MULTIPLIERS = {
        "small": 0.7,    # Simple projects
        "medium": 1.0,   # Standard projects
        "large": 1.5,    # Complex projects
        "enterprise": 2.0 # Large-scale enterprise projects
    }
    
    # Technology stack complexity factors
    TECH_STACK_FACTORS = {
        "simple": 0.8,    # Single technology (e.g., basic Python script)
        "standard": 1.0,  # Common stack (e.g., Python + SQL)
        "complex": 1.3,   # Multiple technologies (e.g., Full-stack application)
        "advanced": 1.6   # Advanced stack (e.g., Microservices, ML, etc.)
    }

    def __init__(self):
        self.progress_mgr = ProgressManager()

    def analyze_project_complexity(self, description: str) -> Tuple[str, str]:
        """
        Analyzes project description to determine complexity and tech stack level
        """
        # Count key indicators
        complexity_indicators = {
            "enterprise": ["enterprise", "large-scale", "multi-team", "corporate"],
            "large": ["complex", "distributed", "scalable", "high-availability"],
            "medium": ["web application", "database", "api", "authentication"],
            "small": ["script", "simple", "basic", "single-user"]
        }
        
        tech_indicators = {
            "advanced": ["machine learning", "ai", "microservices", "kubernetes", "distributed"],
            "complex": ["full-stack", "real-time", "react", "angular", "cloud"],
            "standard": ["database", "api", "authentication", "crud"],
            "simple": ["script", "basic", "command-line", "single-file"]
        }
        
        # Determine project size
        project_size = "medium"  # default
        for size, indicators in complexity_indicators.items():
            if any(indicator in description.lower() for indicator in indicators):
                project_size = size
                break
        
        # Determine tech stack complexity
        tech_level = "standard"  # default
        for level, indicators in tech_indicators.items():
            if any(indicator in description.lower() for indicator in indicators):
                tech_level = level
                break
                
        return project_size, tech_level

    def estimate_project_time(self, project_description: str, team_size: int = 1) -> Dict:
        """
        Estimates project time based on description and team size
        
        Args:
            project_description: Detailed project requirements
            team_size: Number of team members (affects certain phase durations)
            
        Returns:
            Dictionary containing time estimates and breakdowns
        """
        # Analyze project complexity
        project_size, tech_level = self.analyze_project_complexity(project_description)
        
        # Get complexity multipliers
        size_multiplier = self.COMPLEXITY_MULTIPLIERS[project_size]
        tech_multiplier = self.TECH_STACK_FACTORS[tech_level]
        
        # Calculate team efficiency factor (diminishing returns after 3 people)
        team_factor = 1.0 if team_size <= 1 else 1.0 + (0.2 * min(team_size - 1, 2))
        
        # Calculate phase times
        phase_estimates = {}
        total_minutes = 0
        
        with self.progress_mgr.progress:
            console.print("[bold blue]Analyzing Project Requirements and Estimating Timeline[/bold blue]")
            
            # Initialize tasks with base estimates
            for phase, base_time in self.BASE_PHASE_TIMES.items():
                # Apply multipliers
                adjusted_time = base_time * size_multiplier * tech_multiplier
                # Apply team factor for relevant phases
                if phase in ["Development Planning", "System Architecture Design", "QA Strategy"]:
                    adjusted_time /= team_factor
                
                phase_estimates[phase] = round(adjusted_time)
                total_minutes += phase_estimates[phase]
                
                # Add to progress tracker (convert minutes to seconds for the tracker)
                self.progress_mgr.add_task(phase, phase_estimates[phase] * 60)
            
            # Simulate analysis for visual feedback
            for phase in phase_estimates.keys():
                self.progress_mgr.start_task(phase)
                time.sleep(1)  # Brief pause for visualization
                self.progress_mgr.complete_task(phase)
        
        # Create the results dictionary
        results = {
            "total_hours": round(total_minutes / 60, 1),
            "total_minutes": total_minutes,
            "phase_breakdown": phase_estimates,
            "project_complexity": project_size,
            "tech_complexity": tech_level,
            "team_size": team_size,
            "team_efficiency": round(team_factor * 100, 1)
        }
        
        self._display_estimate(results)
        return results

    def _display_estimate(self, results: Dict):
        """Displays formatted estimation results"""
        console.print("\n[bold green]Project Time Estimation Complete[/bold green]")
        
        # Create main estimate panel
        main_panel = Panel(
            f"[bold]Project Overview[/bold]\n\n"
            f"Total Time: {results['total_hours']} hours ({results['total_minutes']} minutes)\n"
            f"Project Complexity: {results['project_complexity'].title()}\n"
            f"Technical Complexity: {results['tech_complexity'].title()}\n"
            f"Team Size: {results['team_size']} members\n"
            f"Team Efficiency: {results['team_efficiency']}%",
            title="Project Time Estimate",
            border_style="blue"
        )
        console.print(main_panel)
        
        # Create breakdown table
        table = Table(title="Phase Breakdown", show_header=True, header_style="bold magenta")
        table.add_column("Phase", style="cyan")
        table.add_column("Estimated Time (minutes)", justify="right")
        
        for phase, minutes in results['phase_breakdown'].items():
            table.add_row(phase, str(minutes))
            
        console.print(table)

def get_project_requirements():
    """Interactive function to gather project requirements from the user"""
    console.print("[bold blue]Welcome to the AI Development Crew Project Estimator![/bold blue]\n")
    
    # Get project type
    console.print("[yellow]What type of application would you like to develop?[/yellow]")
    console.print("1. Web Application")
    console.print("2. Mobile Application")
    console.print("3. Desktop Application")
    console.print("4. API Service")
    console.print("5. Machine Learning System")
    console.print("6. Other (custom description)")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-6): "))
            if 1 <= choice <= 6:
                break
            else:
                console.print("[red]Please enter a number between 1 and 6[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number[/red]")

    # Template descriptions for each type
    templates = {
        1: """Web Application with:
- User authentication and management
- Frontend interface
- Backend API
- Database integration
- Deployment configuration""",
        2: """Mobile Application with:
- User interface
- Data management
- API integration
- Push notifications
- App store deployment""",
        3: """Desktop Application with:
- User interface
- Local data storage
- System integration
- Installation package
- Auto-update mechanism""",
        4: """API Service with:
- Endpoint definitions
- Authentication/Authorization
- Data processing
- Documentation
- Monitoring""",
        5: """Machine Learning System with:
- Data preprocessing
- Model training
- Inference API
- Performance monitoring
- Model versioning"""
    }

    if choice == 6:
        console.print("\n[yellow]Please describe your project requirements:[/yellow]")
        project_description = input()
    else:
        base_description = templates[choice]
        console.print("\n[yellow]Base project description:[/yellow]")
        console.print(base_description)
        console.print("\n[yellow]Would you like to add any specific requirements? (Enter additional requirements or press Enter to continue):[/yellow]")
        additional_reqs = input()
        project_description = base_description + "\n\nAdditional Requirements:\n" + additional_reqs if additional_reqs else base_description

    return project_description

def get_user_confirmation(message: str) -> bool:
    """Get user confirmation for an action"""
    response = input(f"\n{message} (yes/no): ").lower()
    return response in ['y', 'yes']

def main():
    # Get project requirements from user
    project_description = get_project_requirements()
    
    # Create estimator with AI crew team size
    estimator = ProjectEstimator()
    dev_crew = DevCrew()
    team_size = len(dev_crew.agents.get_all_agents())  # Get actual number of AI agents
    
    # Generate estimate
    estimate = estimator.estimate_project_time(
        project_description=project_description,
        team_size=team_size
    )
    
    # Ask user if they want to proceed with implementation
    if get_user_confirmation("\n[yellow]Would you like to proceed with the implementation?[/yellow]"):
        console.print("\n[bold green]Starting Development Process[/bold green]")
        
        # Initialize the development process
        result = None
        try:
            # Start with requirements specification
            requirements_task = dev_crew.tasks.create_requirements_specification_task(
                dev_crew.agents.product_owner,
                project_description
            )
            
            console.print("\n[cyan]Step 1: Requirements Specification[/cyan]")
            result = dev_crew.create_development_plan(project_description)
            
            if not get_user_confirmation("\nAre you satisfied with the requirements specification? Would you like to continue?"):
                console.print("[yellow]Development process paused. You can resume later with refined requirements.[/yellow]")
                return
            
            # Continue with subsequent phases...
            console.print("\n[green]Proceeding with development...[/green]")
            
        except Exception as e:
            console.print(f"\n[red]Error during development process:[/red] {str(e)}")
    else:
        console.print("\n[yellow]Project estimation completed. Implementation cancelled.[/yellow]")

if __name__ == "__main__":
    main()
