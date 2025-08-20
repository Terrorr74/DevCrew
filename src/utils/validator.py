"""Validation system for task inputs and outputs."""
from typing import Any, Callable, Dict, List, Optional, TypeVar
from dataclasses import dataclass
from enum import Enum

T = TypeVar('T')

class ValidationSeverity(Enum):
    WARNING = "warning"   # Issue that should be noted but doesn't invalidate the result
    ERROR = "error"      # Issue that makes the result invalid
    CRITICAL = "critical" # Issue that affects the entire process

@dataclass
class ValidationRule:
    """Definition of a validation rule."""
    name: str
    description: str
    validator: Callable[[Any], bool]
    error_message: str
    severity: ValidationSeverity

@dataclass
class ValidationResult:
    """Result of a validation check."""
    is_valid: bool
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]

class TaskValidator:
    """Validator for task inputs and outputs."""
    
    def __init__(self):
        self.input_rules: Dict[str, List[ValidationRule]] = {}
        self.output_rules: Dict[str, List[ValidationRule]] = {}

    def add_input_rule(self, task_type: str, rule: ValidationRule) -> None:
        """Add a validation rule for task input."""
        if task_type not in self.input_rules:
            self.input_rules[task_type] = []
        self.input_rules[task_type].append(rule)

    def add_output_rule(self, task_type: str, rule: ValidationRule) -> None:
        """Add a validation rule for task output."""
        if task_type not in self.output_rules:
            self.output_rules[task_type] = []
        self.output_rules[task_type].append(rule)

    def validate_input(self, task_type: str, input_data: Any) -> ValidationResult:
        """Validate task input data."""
        return self._validate(task_type, input_data, self.input_rules)

    def validate_output(self, task_type: str, output_data: Any) -> ValidationResult:
        """Validate task output data."""
        return self._validate(task_type, output_data, self.output_rules)

    def _validate(
        self,
        task_type: str,
        data: Any,
        rules: Dict[str, List[ValidationRule]]
    ) -> ValidationResult:
        """Perform validation using specified rules."""
        errors = []
        warnings = []

        if task_type not in rules:
            return ValidationResult(True, [], [])

        for rule in rules[task_type]:
            try:
                is_valid = rule.validator(data)
                if not is_valid:
                    validation_issue = {
                        "rule_name": rule.name,
                        "message": rule.error_message
                    }
                    if rule.severity == ValidationSeverity.WARNING:
                        warnings.append(validation_issue)
                    else:
                        errors.append(validation_issue)
            except Exception as e:
                errors.append({
                    "rule_name": rule.name,
                    "message": f"Validation error: {str(e)}"
                })

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )

# Example validation rules
def create_common_validation_rules() -> Dict[str, List[ValidationRule]]:
    """Create common validation rules for different task types."""
    return {
        "requirements_spec": [
            ValidationRule(
                name="non_empty_requirements",
                description="Check if requirements specification is not empty",
                validator=lambda x: bool(x and x.strip()),
                error_message="Requirements specification cannot be empty",
                severity=ValidationSeverity.ERROR
            ),
            ValidationRule(
                name="min_requirements_length",
                description="Check if requirements have sufficient detail",
                validator=lambda x: len(x.split()) >= 50,
                error_message="Requirements specification seems too brief",
                severity=ValidationSeverity.WARNING
            )
        ],
        "architecture_design": [
            ValidationRule(
                name="has_components",
                description="Check if architecture design includes component definitions",
                validator=lambda x: "components" in x.lower(),
                error_message="Architecture design must include component definitions",
                severity=ValidationSeverity.ERROR
            ),
            ValidationRule(
                name="has_interfaces",
                description="Check if architecture design includes interface definitions",
                validator=lambda x: "interface" in x.lower(),
                error_message="Architecture design should include interface definitions",
                severity=ValidationSeverity.WARNING
            )
        ],
        "code_review": [
            ValidationRule(
                name="has_feedback",
                description="Check if code review includes specific feedback",
                validator=lambda x: len(x.get("feedback", [])) > 0,
                error_message="Code review must include specific feedback points",
                severity=ValidationSeverity.ERROR
            )
        ]
    }
