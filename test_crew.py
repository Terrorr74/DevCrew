import os
import logging
import sys
import time
from rich.console import Console
from rich.panel import Panel
from src.utils.progress_tracker import ProgressManager
from src.main import DevCrew

# Set up rich console
console = Console()

# Set up logging with rich integration
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def test_ai_crew():
    # Phase configurations with estimated durations (in seconds)
    phases = [
        ("Initializing AI Development Crew", 5),
        ("Analyzing Project Requirements", 15),
        ("Creating System Architecture", 20),
        ("Designing Database Schema", 15),
        ("Planning API Endpoints", 20),
        ("Generating Development Plan", 25)
    ]

    try:
        # Initialize progress tracking
        progress_mgr = ProgressManager()
        
        with progress_mgr.progress:
            console.print("[bold blue]Starting AI Development Crew Test[/bold blue]")
            
            # Initialize tasks with estimated durations
            for phase_name, duration in phases:
                progress_mgr.add_task(phase_name, duration)

            # Initialize the DevCrew
            dev_crew = DevCrew()

            project_description = """
            Create a REST API service for a task management system with the following features:
            
            1. User Management:
               - User registration and authentication
               - Role-based access control (Admin, Manager, User)
               
            2. Task Management:
               - Create, read, update, delete tasks
               - Assign tasks to users
               - Set priorities and deadlines
               - Add comments and attachments
               
            3. Project Organization:
               - Group tasks into projects
               - Track project progress
               - Generate project reports
               
            4. Notifications:
               - Email notifications for task assignments
               - Due date reminders
               - Status update notifications
               
            Technical Requirements:
            - Python FastAPI backend
            - PostgreSQL database
            - JWT authentication
            - RESTful API design
            - Swagger documentation
            - Docker containerization
            """

            try:
                # Execute each phase
                for phase_name, _ in phases:
                    progress_mgr.start_task(phase_name)
                    
                    # Update progress every second while the AI works
                    start_time = time.time()
                    while True:
                        progress_mgr.update_progress()
                        
                        # Simulate AI work (replace with actual AI operations)
                        time.sleep(0.5)
                        
                        if time.time() - start_time >= 2:  # Simulated completion after 2 seconds
                            break
                    
                    progress_mgr.complete_task(phase_name)

                # Generate final plan
                result = dev_crew.create_development_plan(project_description)
                
                # Show success message and timing report
                console.print("\n[bold green]Development Plan Created Successfully![/bold green]")
                console.print(Panel(str(result), title="Development Plan Results", border_style="green"))
                console.print(progress_mgr.generate_report())
                
                return True

            except Exception as e:
                console.print(Panel(f"[bold red]Error:[/bold red] {str(e)}", 
                                  title="Phase Error",
                                  border_style="red"))
                return False

    except Exception as e:
        console.print(f"[bold red]Critical Error:[/bold red] {str(e)}")
        return False

if __name__ == "__main__":
    test_ai_crew()
