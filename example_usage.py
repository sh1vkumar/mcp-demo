#!/usr/bin/env python3
"""
Example usage of the Claude Efficiency Tools MCP Server

This script demonstrates how to use the various tools and resources
provided by the MCP server for day-to-day efficiency tasks.
"""

import json
import subprocess
import sys
from pathlib import Path

def run_mcp_command(command_data):
    """Run an MCP command and return the result"""
    try:
        # This is a simplified example - in practice, you'd use the MCP client
        # to communicate with the server
        print(f"Executing: {command_data}")
        return {"success": True, "result": "Example result"}
    except Exception as e:
        return {"error": str(e)}

def demonstrate_file_management():
    """Demonstrate file management tools"""
    print("=== File Management Examples ===\n")
    
    # List files in current directory
    print("1. Listing files in current directory:")
    result = run_mcp_command({
        "tool": "list_files",
        "args": {"directory": ".", "pattern": "*.py"}
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")
    
    # Search for specific content
    print("2. Searching for 'def' in Python files:")
    result = run_mcp_command({
        "tool": "search_files",
        "args": {"directory": ".", "query": "def", "file_type": "*.py"}
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")
    
    # Create a new file
    print("3. Creating a new example file:")
    result = run_mcp_command({
        "tool": "create_file",
        "args": {
            "file_path": "example_output.txt",
            "content": "# This is an example file\n# Created by the MCP server\n",
            "overwrite": False
        }
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")

def demonstrate_system_tools():
    """Demonstrate system and environment tools"""
    print("=== System Tools Examples ===\n")
    
    # Get system information
    print("1. Getting system information:")
    result = run_mcp_command({
        "tool": "get_system_info",
        "args": {}
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")
    
    # Run a simple command
    print("2. Running a system command:")
    result = run_mcp_command({
        "tool": "run_command",
        "args": {"command": "echo 'Hello from MCP!'", "working_directory": "."}
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")
    
    # Get environment variable
    print("3. Getting PATH environment variable:")
    result = run_mcp_command({
        "tool": "get_environment_variable",
        "args": {"name": "PATH"}
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")

def demonstrate_time_tools():
    """Demonstrate time and scheduling tools"""
    print("=== Time Tools Examples ===\n")
    
    # Get current time
    print("1. Getting current time:")
    result = run_mcp_command({
        "tool": "get_current_time",
        "args": {"timezone": "local"}
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")
    
    # Calculate time difference
    print("2. Calculating time difference:")
    result = run_mcp_command({
        "tool": "calculate_time_difference",
        "args": {
            "start_time": "2024-01-01T09:00:00",
            "end_time": "2024-01-01T17:00:00",
            "format": "iso"
        }
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")

def demonstrate_text_processing():
    """Demonstrate text processing tools"""
    print("=== Text Processing Examples ===\n")
    
    sample_text = "This is a sample text for analysis. It contains multiple sentences and words."
    
    # Count words
    print("1. Analyzing text statistics:")
    result = run_mcp_command({
        "tool": "count_words",
        "args": {"text": sample_text}
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")
    
    # Format text
    print("2. Formatting text:")
    result = run_mcp_command({
        "tool": "format_text",
        "args": {"text": "  messy   text   with   spaces  ", "format_type": "clean"}
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")
    
    # Convert data
    print("3. Converting JSON data:")
    json_data = '{"name": "John", "age": 30, "city": "New York"}'
    result = run_mcp_command({
        "tool": "convert_data",
        "args": {
            "data": json_data,
            "from_format": "json",
            "to_format": "json"
        }
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")

def demonstrate_claude_prompts():
    """Demonstrate Claude-specific prompts"""
    print("=== Claude Prompts Examples ===\n")
    
    # Code review prompt
    print("1. Code review prompt:")
    result = run_mcp_command({
        "prompt": "code_review_prompt",
        "args": {"file_path": "main.py", "focus_areas": "security,performance"}
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")
    
    # Documentation prompt
    print("2. Documentation prompt:")
    sample_code = "def calculate_area(radius):\n    return 3.14159 * radius * radius"
    result = run_mcp_command({
        "prompt": "documentation_prompt",
        "args": {"code_content": sample_code, "doc_type": "function"}
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")
    
    # Debugging prompt
    print("3. Debugging prompt:")
    result = run_mcp_command({
        "prompt": "debugging_prompt",
        "args": {
            "error_message": "ModuleNotFoundError: No module named 'requests'",
            "code_context": "import requests\nresponse = requests.get('https://api.example.com')"
        }
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")

def demonstrate_resources():
    """Demonstrate MCP resources"""
    print("=== Resources Examples ===\n")
    
    # File content resource
    print("1. Accessing file content resource:")
    result = run_mcp_command({
        "resource": "file://main.py"
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")
    
    # Project info resource
    print("2. Accessing project information resource:")
    result = run_mcp_command({
        "resource": "project://mcp-demo"
    })
    print(f"Result: {json.dumps(result, indent=2)}\n")

def main():
    """Main function to demonstrate all tools"""
    print("🚀 Claude Efficiency Tools - MCP Server Examples\n")
    print("This script demonstrates the various tools and resources")
    print("available in the MCP server for day-to-day efficiency.\n")
    
    try:
        demonstrate_file_management()
        demonstrate_system_tools()
        demonstrate_time_tools()
        demonstrate_text_processing()
        demonstrate_claude_prompts()
        demonstrate_resources()
        
        print("✅ All examples completed successfully!")
        print("\nTo use these tools with Claude:")
        print("1. Start the MCP server: uv run server main stdio")
        print("2. Connect Claude to the server")
        print("3. Ask Claude to use any of these tools!")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
