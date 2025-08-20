"""
Pytest configuration for the AI Crew Development tests.
"""
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--show-progress",
        action="store_true",
        default=True,
        help="Show progress bars during test execution"
    )

@pytest.fixture(autouse=True)
def _show_progress_bars(request):
    """Fixture to control progress bar display"""
    return request.config.getoption("--show-progress")
