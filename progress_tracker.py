import time
from datetime import datetime, timedelta
from typing import Dict, Optional
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

class TaskTracker:
    def __init__(self, task_name: str, estimated_duration: int):
        self.start_time = None
        self.end_time = None
        self.task_name = task_name
        self.estimated_duration = estimated_duration  # in seconds
        self.actual_duration = None

    def start(self):
        self.start_time = datetime.now()

    def complete(self):
        if self.start_time:
            self.end_time = datetime.now()
            self.actual_duration = (self.end_time - self.start_time).total_seconds()

    @property
    def is_running(self) -> bool:
        return self.start_time is not None and self.end_time is None

    @property
    def progress(self) -> float:
        if not self.start_time:
            return 0.0
        if self.end_time:
            return 1.0
        elapsed = (datetime.now() - self.start_time).total_seconds()
        return min(elapsed / self.estimated_duration, 0.95)  # Cap at 95% until complete

class ProgressManager:
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
        self.current_phase = None

    def add_task(self, description: str, estimated_duration: int) -> str:
        """Add a new task with estimated duration in seconds"""
        task_id = self.progress.add_task(
            f"[cyan]{description}",
            total=100,
            start=False
        )
        tracker = TaskTracker(description, estimated_duration)
        self.tasks[description] = (task_id, tracker)
        return description

    def start_task(self, description: str):
        """Start tracking a task"""
        if description in self.tasks:
            task_id, tracker = self.tasks[description]
            tracker.start()
            self.progress.start_task(task_id)
            self.current_phase = description

    def complete_task(self, description: str):
        """Mark a task as completed"""
        if description in self.tasks:
            task_id, tracker = self.tasks[description]
            tracker.complete()
            self.progress.update(task_id, completed=100)

    def update_progress(self):
        """Update progress for all running tasks"""
        for description, (task_id, tracker) in self.tasks.items():
            if tracker.is_running:
                progress = tracker.progress * 100
                self.progress.update(task_id, completed=progress)

    def generate_report(self) -> Text:
        """Generate a report of task durations"""
        report = Text()
        report.append("\nTask Duration Report\n", style="bold")
        report.append("=" * 50 + "\n")
        
        for description, (_, tracker) in self.tasks.items():
            if tracker.actual_duration:
                report.append(f"\nTask: {description}\n", style="cyan")
                report.append(f"Estimated: {tracker.estimated_duration:.1f}s\n")
                report.append(f"Actual: {tracker.actual_duration:.1f}s\n")
                
                diff = tracker.actual_duration - tracker.estimated_duration
                if abs(diff) > tracker.estimated_duration * 0.1:  # More than 10% off
                    style = "red" if diff > 0 else "green"
                    report.append(f"Difference: {diff:+.1f}s\n", style=style)
                else:
                    report.append(f"Difference: {diff:+.1f}s\n", style="yellow")
                
        return report
