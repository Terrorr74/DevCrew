"""
Progress tracking utilities for monitoring and reporting task execution.
"""

import time
from datetime import datetime, timedelta
from typing import Dict, Optional
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

class TaskTracker:
    """
    Tracks the execution time and progress of a single task.
    
    Attributes:
        task_name (str): Name of the task being tracked
        estimated_duration (int): Expected duration in seconds
        start_time (datetime, optional): When the task started
        end_time (datetime, optional): When the task completed
        actual_duration (float, optional): Actual time taken in seconds
    """
    
    def __init__(self, task_name: str, estimated_duration: int):
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None
        self.task_name = task_name
        self.estimated_duration = estimated_duration  # in seconds
        self.actual_duration: Optional[float] = None

    def start(self) -> None:
        """Start tracking the task execution time."""
        self.start_time = datetime.now()

    def complete(self) -> None:
        """Mark the task as complete and calculate its duration."""
        if self.start_time:
            self.end_time = datetime.now()
            self.actual_duration = (self.end_time - self.start_time).total_seconds()

    @property
    def is_running(self) -> bool:
        """Check if the task is currently running."""
        return self.start_time is not None and self.end_time is None

    @property
    def progress(self) -> float:
        """Calculate the current progress as a percentage (0.0 to 1.0)."""
        if not self.start_time:
            return 0.0
        if self.end_time:
            return 1.0
        elapsed = (datetime.now() - self.start_time).total_seconds()
        return min(elapsed / self.estimated_duration, 0.95)  # Cap at 95% until complete

class ProgressManager:
    """
    Manages progress tracking for multiple tasks with rich console output.
    
    Features:
    - Real-time progress updates
    - Estimated time remaining
    - Task completion statistics
    - Duration analysis
    """
    
    def __init__(self):
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
            console=console
        )
        self.tasks: Dict[str, tuple] = {}  # (progress_id, TaskTracker)
        self.current_phase: Optional[str] = None

    def add_task(self, description: str, estimated_duration: int) -> str:
        """
        Add a new task with estimated duration.
        
        Args:
            description: Task name/description
            estimated_duration: Expected duration in seconds
            
        Returns:
            description: Task identifier
        """
        task_id = self.progress.add_task(
            f"[cyan]{description}",
            total=100,
            start=False
        )
        tracker = TaskTracker(description, estimated_duration)
        self.tasks[description] = (task_id, tracker)
        return description

    def start_task(self, description: str) -> None:
        """
        Start tracking a specific task.
        
        Args:
            description: Task identifier
        """
        if description in self.tasks:
            task_id, tracker = self.tasks[description]
            tracker.start()
            self.progress.start_task(task_id)
            self.current_phase = description

    def complete_task(self, description: str) -> None:
        """
        Mark a task as completed.
        
        Args:
            description: Task identifier
        """
        if description in self.tasks:
            task_id, tracker = self.tasks[description]
            tracker.complete()
            self.progress.update(task_id, completed=100)

    def update_progress(self) -> None:
        """Update progress for all running tasks."""
        for description, (task_id, tracker) in self.tasks.items():
            if tracker.is_running:
                progress = tracker.progress * 100
                self.progress.update(task_id, completed=progress)

    def generate_report(self) -> Text:
        """
        Generate a detailed timing report.
        
        Returns:
            Text: Rich-formatted report showing estimated vs actual durations
        """
        report = Text()
        report.append("\nTask Duration Report\n", style="bold")
        report.append("=" * 50 + "\n")
        
        total_estimated = 0
        total_actual = 0
        
        for description, (_, tracker) in self.tasks.items():
            if tracker.actual_duration:
                total_estimated += tracker.estimated_duration
                total_actual += tracker.actual_duration
                
                report.append(f"\nTask: {description}\n", style="cyan")
                report.append(f"Estimated: {tracker.estimated_duration:.1f}s\n")
                report.append(f"Actual: {tracker.actual_duration:.1f}s\n")
                
                diff = tracker.actual_duration - tracker.estimated_duration
                if abs(diff) > tracker.estimated_duration * 0.1:  # More than 10% off
                    style = "red" if diff > 0 else "green"
                    report.append(f"Difference: {diff:+.1f}s\n", style=style)
                else:
                    report.append(f"Difference: {diff:+.1f}s\n", style="yellow")
        
        if total_actual > 0:
            report.append("\nOverall Summary\n", style="bold blue")
            report.append("-" * 30 + "\n")
            report.append(f"Total Estimated: {total_estimated:.1f}s\n")
            report.append(f"Total Actual: {total_actual:.1f}s\n")
            accuracy = (total_estimated / total_actual - 1) * 100
            report.append(f"Estimation Accuracy: {accuracy:+.1f}%\n", 
                        style="green" if abs(accuracy) < 10 else "red")
        
        return report
