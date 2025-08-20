"""Monitoring system for task execution and error patterns."""
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum

class MetricType(Enum):
    DURATION = "duration"
    ERROR_COUNT = "error_count"
    SUCCESS_RATE = "success_rate"
    RECOVERY_RATE = "recovery_rate"
    VALIDATION_RATE = "validation_rate"

@dataclass
class TaskMetrics:
    """Metrics for a specific task."""
    task_name: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    error_count: int = 0
    recovery_attempts: int = 0
    successful_recoveries: int = 0
    validation_attempts: int = 0
    validation_passes: int = 0
    checkpoint_times: Dict[str, datetime] = field(default_factory=dict)
    error_patterns: Dict[str, int] = field(default_factory=lambda: defaultdict(int))

    @property
    def duration(self) -> Optional[timedelta]:
        """Calculate task duration."""
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None

    @property
    def success_rate(self) -> float:
        """Calculate success rate including recoveries."""
        total_incidents = self.error_count
        if total_incidents == 0:
            return 1.0
        return self.successful_recoveries / total_incidents

    @property
    def validation_success_rate(self) -> float:
        """Calculate validation success rate."""
        if self.validation_attempts == 0:
            return 1.0
        return self.validation_passes / self.validation_attempts

class TaskMonitor:
    """Monitor and analyze task execution patterns."""
    
    def __init__(self):
        self.task_metrics: Dict[str, TaskMetrics] = {}
        self.global_patterns: Dict[str, int] = defaultdict(int)
        self.alert_thresholds: Dict[str, float] = {}

    def start_task(self, task_name: str) -> None:
        """Start monitoring a task."""
        self.task_metrics[task_name] = TaskMetrics(
            task_name=task_name,
            start_time=datetime.now()
        )

    def end_task(self, task_name: str) -> None:
        """End task monitoring."""
        if task_name in self.task_metrics:
            self.task_metrics[task_name].end_time = datetime.now()

    def record_error(
        self,
        task_name: str,
        error_type: str,
        error_context: Dict[str, Any]
    ) -> None:
        """Record an error occurrence."""
        if task_name in self.task_metrics:
            metrics = self.task_metrics[task_name]
            metrics.error_count += 1
            metrics.error_patterns[error_type] += 1
            self.global_patterns[error_type] += 1

    def record_recovery_attempt(
        self,
        task_name: str,
        successful: bool
    ) -> None:
        """Record a recovery attempt."""
        if task_name in self.task_metrics:
            metrics = self.task_metrics[task_name]
            metrics.recovery_attempts += 1
            if successful:
                metrics.successful_recoveries += 1

    def record_validation(
        self,
        task_name: str,
        passed: bool
    ) -> None:
        """Record a validation attempt."""
        if task_name in self.task_metrics:
            metrics = self.task_metrics[task_name]
            metrics.validation_attempts += 1
            if passed:
                metrics.validation_passes += 1

    def record_checkpoint(
        self,
        task_name: str,
        checkpoint_name: str
    ) -> None:
        """Record a task checkpoint."""
        if task_name in self.task_metrics:
            self.task_metrics[task_name].checkpoint_times[checkpoint_name] = datetime.now()

    def get_task_summary(self, task_name: str) -> Dict[str, Any]:
        """Get summary metrics for a task."""
        if task_name not in self.task_metrics:
            return {}

        metrics = self.task_metrics[task_name]
        return {
            "duration": metrics.duration,
            "error_count": metrics.error_count,
            "success_rate": metrics.success_rate,
            "validation_rate": metrics.validation_success_rate,
            "checkpoints": metrics.checkpoint_times,
            "error_patterns": dict(metrics.error_patterns)
        }

    def get_global_patterns(self) -> Dict[str, Any]:
        """Get global error patterns."""
        return {
            "total_errors": sum(self.global_patterns.values()),
            "error_types": dict(self.global_patterns),
            "most_common_errors": sorted(
                self.global_patterns.items(),
                key=lambda x: x[1],
                reverse=True
            )[:5]
        }

    def set_alert_threshold(
        self,
        metric_type: MetricType,
        threshold: float
    ) -> None:
        """Set an alert threshold for a metric."""
        self.alert_thresholds[metric_type.value] = threshold

    def check_alerts(self) -> List[Dict[str, Any]]:
        """Check for metric threshold violations."""
        alerts = []
        for task_name, metrics in self.task_metrics.items():
            if MetricType.ERROR_COUNT.value in self.alert_thresholds:
                threshold = self.alert_thresholds[MetricType.ERROR_COUNT.value]
                if metrics.error_count > threshold:
                    alerts.append({
                        "task_name": task_name,
                        "metric": MetricType.ERROR_COUNT.value,
                        "current_value": metrics.error_count,
                        "threshold": threshold
                    })

            if MetricType.SUCCESS_RATE.value in self.alert_thresholds:
                threshold = self.alert_thresholds[MetricType.SUCCESS_RATE.value]
                if metrics.success_rate < threshold:
                    alerts.append({
                        "task_name": task_name,
                        "metric": MetricType.SUCCESS_RATE.value,
                        "current_value": metrics.success_rate,
                        "threshold": threshold
                    })

        return alerts
