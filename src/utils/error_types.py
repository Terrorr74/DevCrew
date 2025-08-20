"""Custom error types for better error handling in the AI Crew system."""
from enum import Enum
from typing import Any, Dict, Optional

class ErrorSeverity(Enum):
    LOW = "low"        # Minor issues that don't affect the overall process
    MEDIUM = "medium"  # Issues that might affect quality but don't stop execution
    HIGH = "high"      # Critical issues that require immediate attention
    FATAL = "fatal"    # Issues that force process termination

class ErrorCategory(Enum):
    MODEL_ERROR = "model_error"           # AI model-related errors
    CONTEXT_ERROR = "context_error"       # Issues with context or dependencies
    VALIDATION_ERROR = "validation_error" # Output validation failures
    RESOURCE_ERROR = "resource_error"     # System resource issues
    TIMEOUT_ERROR = "timeout_error"       # Task execution timeout
    INPUT_ERROR = "input_error"          # Invalid input data
    LOGIC_ERROR = "logic_error"          # Business logic violations

class TaskExecutionError(Exception):
    """Base exception for task execution errors with detailed context."""
    
    def __init__(
        self,
        message: str,
        task_name: str,
        severity: ErrorSeverity,
        category: ErrorCategory,
        context: Optional[Dict[str, Any]] = None,
        recovery_hint: Optional[str] = None
    ):
        self.message = message
        self.task_name = task_name
        self.severity = severity
        self.category = category
        self.context = context or {}
        self.recovery_hint = recovery_hint
        super().__init__(self.message)

class ModelExecutionError(TaskExecutionError):
    """Raised when the AI model fails to generate valid output."""
    
    def __init__(
        self,
        message: str,
        task_name: str,
        model_name: str,
        prompt_info: Dict[str, Any],
        severity: ErrorSeverity = ErrorSeverity.HIGH,
        recovery_hint: Optional[str] = None
    ):
        super().__init__(
            message=message,
            task_name=task_name,
            severity=severity,
            category=ErrorCategory.MODEL_ERROR,
            context={
                "model_name": model_name,
                "prompt_info": prompt_info
            },
            recovery_hint=recovery_hint
        )

class ValidationError(TaskExecutionError):
    """Raised when task output fails validation."""
    
    def __init__(
        self,
        message: str,
        task_name: str,
        validation_errors: Dict[str, str],
        severity: ErrorSeverity = ErrorSeverity.MEDIUM,
        recovery_hint: Optional[str] = None
    ):
        super().__init__(
            message=message,
            task_name=task_name,
            severity=severity,
            category=ErrorCategory.VALIDATION_ERROR,
            context={"validation_errors": validation_errors},
            recovery_hint=recovery_hint
        )

class ContextError(TaskExecutionError):
    """Raised when there are issues with task context or dependencies."""
    
    def __init__(
        self,
        message: str,
        task_name: str,
        missing_dependencies: list[str],
        severity: ErrorSeverity = ErrorSeverity.HIGH,
        recovery_hint: Optional[str] = None
    ):
        super().__init__(
            message=message,
            task_name=task_name,
            severity=severity,
            category=ErrorCategory.CONTEXT_ERROR,
            context={"missing_dependencies": missing_dependencies},
            recovery_hint=recovery_hint
        )
