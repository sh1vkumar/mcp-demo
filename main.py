"""
Enhanced MCP Server for Claude with Day-to-Day Efficiency Tools

This server provides various tools to improve daily productivity and efficiency
when working with Claude through MCP.

Usage:
    uv run server main stdio
"""

import os
import json
import datetime
import subprocess
import platform
from pathlib import Path
from typing import List, Dict, Optional, Any
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Claude Efficiency Tools")

# Server initialization is handled automatically by FastMCP

# ============================================================================
# FILE AND PROJECT MANAGEMENT TOOLS
# ============================================================================

@mcp.tool()
def list_files(directory: str = ".", pattern: str = "*") -> Dict[str, Any]:
    """List files in a directory with optional pattern matching"""
    try:
        path = Path(directory).resolve()
        files = list(path.glob(pattern))
        return {
            "directory": str(path),
            "pattern": pattern,
            "files": [str(f.relative_to(path)) for f in files if f.is_file()],
            "directories": [str(f.relative_to(path)) for f in files if f.is_dir()],
            "total_files": len([f for f in files if f.is_file()]),
            "total_dirs": len([f for f in files if f.is_dir()])
        }
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def search_files(directory: str = ".", query: str = "", file_type: str = "*") -> Dict[str, Any]:
    """Search for files containing specific text or matching patterns"""
    try:
        path = Path(directory).resolve()
        pattern = f"*{file_type}" if file_type != "*" else "*"
        files = list(path.rglob(pattern))
        
        results = []
        for file in files:
            if file.is_file():
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if query.lower() in content.lower():
                            results.append({
                                "file": str(file.relative_to(path)),
                                "size": file.stat().st_size,
                                "modified": datetime.datetime.fromtimestamp(file.stat().st_mtime).isoformat()
                            })
                except:
                    continue
        
        return {
            "directory": str(path),
            "query": query,
            "file_type": file_type,
            "results": results,
            "total_matches": len(results)
        }
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def create_file(file_path: str, content: str = "", overwrite: bool = False) -> Dict[str, Any]:
    """Create a new file with specified content"""
    try:
        path = Path(file_path)
        if path.exists() and not overwrite:
            return {"error": f"File {file_path} already exists. Set overwrite=True to overwrite."}
        
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return {
            "success": True,
            "file_path": str(path.resolve()),
            "size": path.stat().st_size,
            "created": datetime.datetime.fromtimestamp(path.stat().st_ctime).isoformat()
        }
    except Exception as e:
        return {"error": str(e)}

# ============================================================================
# SYSTEM AND ENVIRONMENT TOOLS
# ============================================================================

@mcp.tool()
def get_system_info() -> Dict[str, Any]:
    """Get current system information"""
    return {
        "platform": platform.system(),
        "platform_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "current_directory": str(Path.cwd()),
        "home_directory": str(Path.home()),
        "environment_variables": dict(os.environ)
    }

@mcp.tool()
def run_command(command: str, working_directory: str = ".") -> Dict[str, Any]:
    """Execute a shell command and return the result"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )
        return {
            "command": command,
            "working_directory": working_directory,
            "return_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {"error": "Command timed out after 30 seconds"}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_environment_variable(name: str) -> Dict[str, Any]:
    """Get the value of an environment variable"""
    value = os.environ.get(name)
    return {
        "name": name,
        "value": value,
        "exists": value is not None
    }

# ============================================================================
# TIME AND SCHEDULING TOOLS
# ============================================================================

@mcp.tool()
def get_current_time(timezone: str = "local") -> Dict[str, Any]:
    """Get current time and date information"""
    now = datetime.datetime.now()
    return {
        "current_time": now.isoformat(),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "day_of_week": now.strftime("%A"),
        "timezone": timezone,
        "timestamp": now.timestamp()
    }

@mcp.tool()
def calculate_time_difference(start_time: str, end_time: str, format: str = "iso") -> Dict[str, Any]:
    """Calculate the difference between two times"""
    try:
        if format == "iso":
            start = datetime.datetime.fromisoformat(start_time)
            end = datetime.datetime.fromisoformat(end_time)
        else:
            start = datetime.datetime.strptime(start_time, format)
            end = datetime.datetime.strptime(end_time, format)
        
        diff = end - start
        return {
            "start_time": start.isoformat(),
            "end_time": end.isoformat(),
            "difference_seconds": diff.total_seconds(),
            "difference_minutes": diff.total_seconds() / 60,
            "difference_hours": diff.total_seconds() / 3600,
            "difference_days": diff.days,
            "formatted": str(diff)
        }
    except Exception as e:
        return {"error": str(e)}

# ============================================================================
# TEXT PROCESSING AND UTILITY TOOLS
# ============================================================================

@mcp.tool()
def count_words(text: str) -> Dict[str, Any]:
    """Analyze text and provide word count statistics"""
    words = text.split()
    characters = len(text)
    characters_no_spaces = len(text.replace(" ", ""))
    
    return {
        "word_count": len(words),
        "character_count": characters,
        "character_count_no_spaces": characters_no_spaces,
        "line_count": len(text.splitlines()),
        "average_word_length": sum(len(word) for word in words) / len(words) if words else 0,
        "unique_words": len(set(words))
    }

@mcp.tool()
def format_text(text: str, format_type: str = "clean") -> Dict[str, Any]:
    """Format text in various ways"""
    if format_type == "clean":
        # Remove extra whitespace and normalize
        formatted = " ".join(text.split())
    elif format_type == "uppercase":
        formatted = text.upper()
    elif format_type == "lowercase":
        formatted = text.lower()
    elif format_type == "title":
        formatted = text.title()
    elif format_type == "sentence":
        formatted = ". ".join(s.capitalize().strip() for s in text.split("."))
    else:
        formatted = text
    
    return {
        "original": text,
        "formatted": formatted,
        "format_type": format_type,
        "length_change": len(formatted) - len(text)
    }

# ============================================================================
# DATA CONVERSION TOOLS
# ============================================================================

@mcp.tool()
def convert_data(data: str, from_format: str, to_format: str) -> Dict[str, Any]:
    """Convert data between different formats (JSON, YAML, etc.)"""
    try:
        if from_format == "json":
            parsed = json.loads(data)
        else:
            return {"error": f"Unsupported input format: {from_format}"}
        
        if to_format == "json":
            result = json.dumps(parsed, indent=2)
        elif to_format == "compact_json":
            result = json.dumps(parsed)
        else:
            return {"error": f"Unsupported output format: {to_format}"}
        
        return {
            "success": True,
            "from_format": from_format,
            "to_format": to_format,
            "result": result,
            "size": len(result)
        }
    except Exception as e:
        return {"error": str(e)}

# ============================================================================
# PROMPT TEMPLATES FOR CLAUDE
# ============================================================================

@mcp.prompt()
def code_review_prompt(file_path: str, focus_areas: str = "all") -> str:
    """Generate a code review prompt for Claude"""
    return f"""Please review the code in {file_path}. Focus on the following areas: {focus_areas}.

Please provide:
1. Code quality assessment
2. Potential bugs or issues
3. Performance improvements
4. Security considerations
5. Best practices recommendations
6. Specific suggestions for improvement

Be thorough but constructive in your feedback."""

@mcp.prompt()
def documentation_prompt(code_content: str, doc_type: str = "function") -> str:
    """Generate a documentation prompt for Claude"""
    return f"""Please create {doc_type} documentation for the following code:

{code_content}

Please provide:
1. Clear and concise documentation
2. Parameter descriptions
3. Return value descriptions
4. Usage examples
5. Any important notes or warnings

Make the documentation comprehensive and easy to understand."""

@mcp.prompt()
def debugging_prompt(error_message: str, code_context: str = "") -> str:
    """Generate a debugging prompt for Claude"""
    return f"""I'm encountering this error:

{error_message}

Code context:
{code_context}

Please help me:
1. Identify the root cause of the error
2. Suggest specific fixes
3. Explain why this error occurred
4. Provide best practices to prevent similar issues
5. If possible, provide corrected code

Be detailed in your analysis and solutions."""

@mcp.prompt()
def optimization_prompt(code_content: str, optimization_goal: str = "performance") -> str:
    """Generate an optimization prompt for Claude"""
    return f"""Please analyze this code for {optimization_goal} optimization:

{code_content}

Please provide:
1. Current performance analysis
2. Specific optimization opportunities
3. Code improvements with explanations
4. Alternative approaches
5. Trade-offs to consider
6. Benchmarking suggestions

Focus on practical, actionable improvements."""

# ============================================================================
# RESOURCES FOR CLAUDE
# ============================================================================

@mcp.resource("file://{file_path}")
def get_file_content(file_path: str) -> str:
    """Get the content of a file as a resource"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file {file_path}: {str(e)}"

@mcp.resource("project://{project_name}")
def get_project_info(project_name: str) -> str:
    """Get project information as a resource"""
    try:
        # Try to read common project files
        files_to_check = [
            "README.md",
            "pyproject.toml",
            "package.json",
            "requirements.txt",
            "setup.py"
        ]
        
        info = f"Project: {project_name}\n\n"
        for file in files_to_check:
            if Path(file).exists():
                with open(file, 'r', encoding='utf-8') as f:
                    info += f"=== {file} ===\n{f.read()}\n\n"
        
        return info
    except Exception as e:
        return f"Error getting project info: {str(e)}"

if __name__ == "__main__":
    # Run the server
    mcp.run()