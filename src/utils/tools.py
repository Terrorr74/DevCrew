"""Tool definitions for AI agents."""
from typing import List, Callable, Any, Dict, Optional
from crewai.tools import BaseTool
import subprocess
import os

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

# Create tool instances
code_analysis_tool = CodeAnalysisTool()
test_runner_tool = TestRunnerTool()
doc_generator_tool = DocGeneratorTool()
file_system_tool = FileSystemTool()

class DevTeamTools:
    """Collection of tools for development team agents."""
    
    @staticmethod
    def get_developer_tools() -> List[BaseTool]:
        """Get tools for the developer agent."""
        return [
            code_analysis_tool,
            test_runner_tool,
            file_system_tool,
            doc_generator_tool
        ]
    
    @staticmethod
    def get_architect_tools() -> List[BaseTool]:
        """Get tools for the architect agent."""
        return [
            code_analysis_tool,
            doc_generator_tool,
            file_system_tool
        ]
    
    @staticmethod
    def get_devops_tools() -> List[BaseTool]:
        """Get tools for the DevOps engineer agent."""
        return [
            file_system_tool,
            code_analysis_tool
        ]
    
    @staticmethod
    def get_qa_tools() -> List[BaseTool]:
        """Get tools for the QA engineer agent."""
        return [
            test_runner_tool,
            file_system_tool,
            code_analysis_tool
        ]
    
    @staticmethod
    def get_product_owner_tools() -> List[BaseTool]:
        """Get tools for the product owner agent."""
        return [
            doc_generator_tool,
            file_system_tool
        ]
    
    @staticmethod
    def get_documentation_tools() -> List[BaseTool]:
        """Get tools for the documentation specialist agent."""
        return [
            doc_generator_tool,
            file_system_tool,
            code_analysis_tool
        ]
