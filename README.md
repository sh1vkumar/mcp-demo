# Claude Efficiency Tools - MCP Server

A comprehensive MCP (Model Context Protocol) server that provides Claude with powerful day-to-day efficiency tools for improved productivity and workflow automation.

## 🚀 Features

### File & Project Management
- **List Files**: Browse directories with pattern matching
- **Search Files**: Find files containing specific text
- **Create Files**: Generate new files with content
- **Project Info**: Get comprehensive project information

### System & Environment Tools
- **System Info**: Get detailed system information
- **Run Commands**: Execute shell commands safely
- **Environment Variables**: Access and manage environment variables

### Time & Scheduling
- **Current Time**: Get detailed time information
- **Time Calculations**: Calculate time differences and durations

### Text Processing
- **Word Count**: Analyze text with detailed statistics
- **Text Formatting**: Clean, format, and transform text
- **Data Conversion**: Convert between JSON formats

### Claude-Specific Prompts
- **Code Review**: Generate comprehensive code review prompts
- **Documentation**: Create documentation prompts for any code
- **Debugging**: Get debugging assistance prompts
- **Optimization**: Generate performance optimization prompts

### Resources
- **File Content**: Access file contents as resources
- **Project Information**: Get project metadata and files

## 📦 Installation

1. **Install Dependencies**:
   ```bash
   uv sync
   ```

2. **Run the Server**:
   ```bash
   uv run server main stdio
   ```

## 🔧 Usage with Claude

### Basic Setup

1. **Start the MCP Server**:
   ```bash
   uv run server main stdio
   ```

2. **Connect Claude to the Server**:
   - Use Claude Desktop or Claude Web with MCP support
   - Configure the server connection in your Claude client
   - The server will provide all tools and resources to Claude

### Example Workflows

#### 1. Project Analysis
```
Claude can now:
- List all files in your project
- Search for specific code patterns
- Get project metadata
- Analyze code structure
```

#### 2. Code Review & Documentation
```
Claude can:
- Review code files automatically
- Generate documentation
- Suggest improvements
- Create optimization recommendations
```

#### 3. File Management
```
Claude can:
- Create new files with content
- Search through existing files
- Organize project structure
- Manage configuration files
```

#### 4. System Operations
```
Claude can:
- Get system information
- Run commands safely
- Check environment variables
- Monitor system status
```

## 🛠️ Available Tools

### File Management Tools

#### `list_files`
Lists files in a directory with optional pattern matching.
```python
list_files(directory=".", pattern="*.py")
```

#### `search_files`
Search for files containing specific text.
```python
search_files(directory=".", query="def main", file_type="*.py")
```

#### `create_file`
Create a new file with specified content.
```python
create_file(file_path="new_script.py", content="# New Python script", overwrite=False)
```

### System Tools

#### `get_system_info`
Get comprehensive system information.
```python
get_system_info()
```

#### `run_command`
Execute shell commands safely.
```python
run_command(command="ls -la", working_directory=".")
```

#### `get_environment_variable`
Get environment variable values.
```python
get_environment_variable(name="PATH")
```

### Time Tools

#### `get_current_time`
Get current time and date information.
```python
get_current_time(timezone="local")
```

#### `calculate_time_difference`
Calculate time differences.
```python
calculate_time_difference(start_time="2024-01-01T10:00:00", end_time="2024-01-01T18:00:00")
```

### Text Processing Tools

#### `count_words`
Analyze text with detailed statistics.
```python
count_words(text="Your text here")
```

#### `format_text`
Format text in various ways.
```python
format_text(text="your text", format_type="clean")
```

#### `convert_data`
Convert data between formats.
```python
convert_data(data='{"key": "value"}', from_format="json", to_format="compact_json")
```

## 📝 Claude Prompts

### Code Review Prompt
```python
code_review_prompt(file_path="main.py", focus_areas="security,performance")
```

### Documentation Prompt
```python
documentation_prompt(code_content="def example(): pass", doc_type="function")
```

### Debugging Prompt
```python
debugging_prompt(error_message="ImportError: No module named 'xyz'", code_context="import xyz")
```

### Optimization Prompt
```python
optimization_prompt(code_content="your code here", optimization_goal="performance")
```

## 🔗 Resources

### File Content Resource
Access file contents directly:
```
file://path/to/your/file.py
```

### Project Information Resource
Get project metadata:
```
project://your-project-name
```

## 🎯 Day-to-Day Efficiency Use Cases

### 1. **Code Development**
- Automatically review new code
- Generate documentation
- Find similar code patterns
- Optimize performance

### 2. **Project Management**
- Analyze project structure
- Search for specific implementations
- Create new files and templates
- Monitor project health

### 3. **System Administration**
- Check system status
- Run maintenance commands
- Monitor environment variables
- Troubleshoot issues

### 4. **Content Creation**
- Analyze text content
- Format documents
- Convert data formats
- Generate reports

### 5. **Time Management**
- Track time spent on tasks
- Calculate project durations
- Schedule reminders
- Analyze productivity patterns

## 🔒 Security Considerations

- The `run_command` tool has a 30-second timeout
- File operations are restricted to the current working directory
- Environment variable access is read-only
- All operations include error handling

## 🚀 Getting Started

1. **Clone or download this project**
2. **Install dependencies**: `uv sync`
3. **Start the server**: `uv run server main stdio`
4. **Connect Claude to the server**
5. **Start using the tools!**

## 📚 Examples

### Example 1: Project Analysis
```
User: "Analyze my current project structure and suggest improvements"
Claude: [Uses list_files, search_files, and project resources to provide comprehensive analysis]
```

### Example 2: Code Review
```
User: "Review the main.py file for security issues"
Claude: [Uses code_review_prompt and file resources to provide detailed security analysis]
```

### Example 3: File Management
```
User: "Create a new configuration file for my project"
Claude: [Uses create_file and project resources to generate appropriate configuration]
```

## 🤝 Contributing

Feel free to extend this server with additional tools and resources that would be useful for your workflow!

## 📄 License

This project is open source and available under the MIT License.
