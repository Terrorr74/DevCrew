"""
Simple test for the DevCrew progress tracking functionality
"""
import time
from rich.console import Console
from rich.panel import Panel
from src.utils.progress_tracker import ProgressManager

console = Console()

def test_progress_tracking():
    """Test the progress tracking functionality with a simple task"""
    # Define a single phase for testing
    phases = [
        ("Simple Test Task", 3)
    ]

    try:
        # Initialize progress tracking
        progress_mgr = ProgressManager()
        
        with progress_mgr.progress:
            console.print("[bold blue]Starting Simple Progress Test[/bold blue]")
            
            # Initialize task with estimated duration
            progress_mgr.add_task(phases[0][0], phases[0][1])
            
            # Execute the task
            progress_mgr.start_task(phases[0][0])
            
            # Simulate work with progress updates
            start_time = time.time()
            while time.time() - start_time < phases[0][1]:
                progress_mgr.update_progress()
                time.sleep(0.1)
            
            progress_mgr.complete_task(phases[0][0])
            
            # Show timing report
            console.print("\n[bold green]Test Task Completed![/bold green]")
            console.print(progress_mgr.generate_report())
            
            # Assert the task completed successfully
            task_info = progress_mgr.tasks[phases[0][0]][1]  # Get the TaskTracker
            assert task_info.actual_duration is not None, "Task should have completed"
            assert task_info.actual_duration >= 2.5, "Task should have run for at least 2.5 seconds"
            assert task_info.actual_duration <= 4.0, "Task should not have taken more than 4 seconds"

    except Exception as e:
        console.print(f"[bold red]Test Error:[/bold red] {str(e)}")
        raise

if __name__ == "__main__":
    test_progress_tracking()
