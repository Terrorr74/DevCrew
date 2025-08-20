"""Tool definitions for AI agents."""
from typing import List, Callable, Any, Dict, Optional, Union
from crewai.tools import BaseTool
import subprocess
import os
from rich.console import Console

console = Console()

def github_search(repo: str, query: str) -> str:
    """Search for code in a GitHub repository."""
    try:
        # Use semantic search for documentation
        cmd = f'gh search code "{query}" --repo {repo} --limit 5'
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            return f"Error searching code: {stderr.decode()}"
        return stdout.decode()
    except Exception as e:
        return f"Error: {str(e)}"
from typing import List, Callable, Any, Dict, Optional, Union
from crewai.tools import BaseTool
import subprocess
import os

from functions import (
    github_repo as mcp_github_search_code
)

def run_command(command: str) -> str:
    """Run a shell command and return its output."""
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        return f"Error: {stderr.decode()}"
    return stdout.decode()

def analyze_code(path: str = ".") -> str:
    """Analyze code using pylint."""
    return run_command(f"find {path} -name '*.py' | xargs pylint")

def run_tests(path: str = "tests/") -> str:
    """Run tests using pytest."""
    return run_command(f"python -m pytest {path} -v")

def generate_docs(path: str = "src/") -> str:
    """Generate documentation using pdoc."""
    return run_command(f"pdoc --html {path}")

def file_operation(command: str) -> str:
    """Execute safe file system operations."""
    safe_commands = ("ls", "find", "cat")
    if any(command.startswith(cmd) for cmd in safe_commands):
        return run_command(command)
    return "Error: Unauthorized command"

class CodeAnalysisTool(BaseTool):
    name: str = "code_analysis"
    description: str = "Analyzes code structure and quality using pylint"

    def _run(
        self,
        filename: str,
        additional_context: Optional[Dict[str, Any]] = None
    ) -> str:
        return analyze_code(filename)

class TestRunnerTool(BaseTool):
    name: str = "test_runner"
    description: str = "Runs pytest tests and returns results"

    def _run(self, path: str = "tests/") -> str:
        return run_tests(path)

class DocGeneratorTool(BaseTool):
    name: str = "doc_generator"
    description: str = "Generates documentation from code using pdoc"

    def _run(self, path: str = "src/") -> str:
        return generate_docs(path)

class FileSystemTool(BaseTool):
    name: str = "file_system"
    description: str = "Manages project files and directories safely"

    def _run(self, command: str) -> str:
        return file_operation(command)

class Context7Tool(BaseTool):
    name: str = "context7"
    description: str = "Get documentation and code examples from libraries"

    def _run(
        self,
        library_name: str,
        query: str
    ) -> str:
        """
        Get documentation and code examples from repositories.

        Args:
            library_name: Name of the library to search for documentation
            query: Specific query or topic to search for in the documentation
        """
        try:
            # Search for code examples and documentation
            result = github_search(library_name, query)
            if not result:
                return f"No documentation found for {library_name}"
                
            # Return the formatted results
            return f"Documentation and examples for {query} in {library_name}:\n\n{result}"
            
        except Exception as e:
            return f"Error fetching documentation: {str(e)}"

# Create tool instances
code_analysis_tool = CodeAnalysisTool()
test_runner_tool = TestRunnerTool()
doc_generator_tool = DocGeneratorTool()
file_system_tool = FileSystemTool()
context7_tool = Context7Tool()

class DevTeamTools:
    """Collection of tools for development team agents."""
    
    @staticmethod
    def get_developer_tools() -> List[BaseTool]:
        """Get tools for the developer agent."""
        return [
            code_analysis_tool,  # For code quality checks
            file_system_tool,    # For file operations
            test_runner_tool,    # For running unit tests
            context7_tool        # For accessing documentation
        ]
    
    @staticmethod
    def get_qa_tools() -> List[BaseTool]:
        """Get tools for the QA engineer agent."""
        return [
            test_runner_tool,    # For running tests
            code_analysis_tool,  # For code quality analysis
            file_system_tool     # For accessing test files and results
        ]
