"""Error handling utilities for the AI Crew system."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any

@dataclass
class TaskError:
    task_name: str
    error_message: str
    timestamp: datetime
    phase: str
    context: Optional[Dict[str, Any]] = None
    recovery_attempted: bool = False

class ErrorHandler:
    def __init__(self):
        self.errors = []
        self.recovery_strategies = {}

    def log_error(self, task_error: TaskError) -> None:
        """Log a task error with context."""
        self.errors.append(task_error)

    def get_task_errors(self, task_name: str) -> list[TaskError]:
        """Get all errors for a specific task."""
        return [error for error in self.errors if error.task_name == task_name]

    def add_recovery_strategy(self, task_name: str, strategy_func) -> None:
        """Register a recovery strategy for a specific task."""
        self.recovery_strategies[task_name] = strategy_func

    def attempt_recovery(self, task_name: str, error: TaskError) -> bool:
        """Attempt to recover from a task error."""
        if task_name in self.recovery_strategies and not error.recovery_attempted:
            try:
                self.recovery_strategies[task_name](error)
                error.recovery_attempted = True
                return True
            except Exception as e:
                error.context = error.context or {}
                error.context['recovery_error'] = str(e)
                return False
        return False

    def get_error_summary(self) -> dict:
        """Get a summary of all errors encountered."""
        return {
            'total_errors': len(self.errors),
            'errors_by_phase': self._group_errors_by_phase(),
            'recovery_attempts': self._count_recovery_attempts()
        }

    def _group_errors_by_phase(self) -> dict:
        """Group errors by their phase."""
        phases = {}
        for error in self.errors:
            if error.phase not in phases:
                phases[error.phase] = []
            phases[error.phase].append({
                'task': error.task_name,
                'message': error.error_message,
                'timestamp': error.timestamp.isoformat()
            })
        return phases

    def _count_recovery_attempts(self) -> dict:
        """Count successful and failed recovery attempts."""
        return {
            'attempted': len([e for e in self.errors if e.recovery_attempted]),
            'total': len(self.errors)
        }
