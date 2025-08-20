"""
Test suite for AI Crew development process.
"""
import time
import pytest
from rich.console import Console
from rich.panel import Panel
from src.utils.progress_tracker import ProgressManager
from src.main import DevCrew

# Set up rich console for test output
console = Console()

@pytest.mark.timeout(300)  # 5 minutes timeout
def test_ai_crew(capsys):
    """
    Test the AI development crew's ability to create a development plan
    with progress tracking and time estimation.
    
    Args:
        capsys: Pytest fixture to capture stdout/stderr
    """
    # Disable pytest output capture to show progress bars
    with capsys.disabled():
        console.print("[bold yellow]Starting AI Development Crew Test Suite[/bold yellow]")
        
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
                report = progress_mgr.generate_report()
                console.print(report)

                # Verify each phase completed successfully
                for phase_name, expected_duration in phases:
                    task_info = progress_mgr.tasks[phase_name][1]  # Get the TaskTracker
                    assert task_info.actual_duration is not None, f"Phase '{phase_name}' should have completed"
                    assert task_info.actual_duration > 0, f"Phase '{phase_name}' should have taken some time"
                    
                    # Check if the actual duration is within reasonable bounds
                    # Allow for some flexibility in timing (0.5x to 2x expected duration)
                    min_duration = expected_duration * 0.5
                    max_duration = expected_duration * 2.0
                    assert min_duration <= task_info.actual_duration <= max_duration, \
                        f"Phase '{phase_name}' took {task_info.actual_duration:.1f}s " \
                        f"(expected between {min_duration:.1f}s and {max_duration:.1f}s)"

                # Verify the development plan result
                assert result is not None, "Development plan should not be None"
                assert isinstance(result, str) and len(result) > 0, "Development plan should not be empty"

                return result  # Return the actual result for further inspection if needed

            except Exception as e:
                # Log the error with full phase information
                error_panel = Panel.fit(
                    f"[bold red]Error during execution:[/bold red]\n{str(e)}\n\n"
                    "[bold yellow]Phase Status:[/bold yellow]"
                    + "\n".join([
                        f"\n{name}: "
                        + ("[green]Complete[/green]" 
                           if progress_mgr.tasks[name][1].end_time is not None
                           else "[red]Incomplete[/red]")
                        for name, _ in phases
                    ]),
                    title="Test Failure Details",
                    border_style="red"
                )
                console.print(error_panel)
                raise  # Re-raise the exception for pytest to catch

    except Exception as e:
        console.print(f"[bold red]Critical Error:[/bold red] {str(e)}")
        raise  # Re-raise the exception for pytest to catch

if __name__ == "__main__":
    pytest.main([__file__])
