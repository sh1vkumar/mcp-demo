# Basic MCP Server Implementation

A simple implementation of a Model Context Protocol (MCP) server that demonstrates core MCP concepts and functionality.

## Overview

This project showcases a basic MCP server implementation that provides:
- Simple tool registration and execution
- Resource management
- Prompt templates
- Basic logging and error handling

The Model Context Protocol (MCP) is an open protocol that enables secure connections between host applications (like Claude Desktop, IDEs, or other AI tools) and external data sources and tools.

## Features

- **Tools**: Demonstrates basic tool implementation with input validation
- **Resources**: Shows how to expose external resources through MCP
- **Prompts**: Includes example prompt templates
- **Error Handling**: Proper error responses and logging
- **Type Safety**: Full TypeScript implementation with proper typing

## Prerequisites

- Node.js 18+ 
- npm or yarn
- TypeScript (for development)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp-server-basic
```

2. Install dependencies:
```bash
npm install
```

3. Build the project:
```bash
npm run build
```

## Usage

### Running the Server

Start the MCP server in stdio mode:
```bash
npm start
```

Or run in development mode with auto-reload:
```bash
npm run dev
```

### Connecting to Claude Desktop

Add the following configuration to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "basic-mcp-server": {
      "command": "node",
      "args": ["path/to/your/server/dist/index.js"],
      "env": {}
    }
  }
}
```

## Project Structure

```
├── src/
│   ├── index.ts          # Main server entry point
│   ├── tools/            # Tool implementations
│   │   ├── calculator.ts # Example calculator tool
│   │   └── filesystem.ts # File system operations
│   ├── resources/        # Resource handlers
│   │   └── files.ts      # File resource management
│   ├── prompts/          # Prompt templates
│   │   └── templates.ts  # Example prompt templates
│   └── types/            # TypeScript type definitions
│       └── mcp.ts        # MCP-specific types
├── dist/                 # Compiled JavaScript
├── package.json
├── tsconfig.json
└── README.md
```

## Available Tools

### Calculator Tool
Performs basic arithmetic operations.

**Usage Example**:
```json
{
  "name": "calculator",
  "arguments": {
    "operation": "add",
    "a": 10,
    "b": 5
  }
}
```

### File System Tool
Basic file operations like reading and writing files.

**Usage Example**:
```json
{
  "name": "read_file",
  "arguments": {
    "path": "./example.txt"
  }
}
```

## Available Resources

### File Resources
Exposes files from specified directories as MCP resources.

**Resource URI Format**: `file://path/to/file.txt`

## Available Prompts

### Code Review Template
A prompt template for code review assistance.

**Prompt Name**: `code_review`
**Arguments**: `code`, `language`, `focus_areas`

## API Reference

### Core MCP Methods

The server implements the following MCP protocol methods:

- `initialize` - Server initialization
- `tools/list` - List available tools
- `tools/call` - Execute a tool
- `resources/list` - List available resources  
- `resources/read` - Read resource content
- `prompts/list` - List available prompts
- `prompts/get` - Get prompt template

### Error Handling

The server returns standardized MCP error responses:

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid params",
    "data": "Additional error context"
  }
}
```

## Development

### Running Tests
```bash
npm test
```

### Linting
```bash
npm run lint
```

### Type Checking
```bash
npm run type-check
```

### Building
```bash
npm run build
```

## Configuration

Environment variables and configuration options:

- `LOG_LEVEL`: Set logging level (debug, info, warn, error)
- `MAX_FILE_SIZE`: Maximum file size for file operations (default: 10MB)
- `ALLOWED_PATHS`: Comma-separated list of allowed file paths

## Troubleshooting

### Common Issues

1. **Server not starting**: Check Node.js version and dependencies
2. **Tool execution failures**: Verify input parameters match expected schema
3. **Permission errors**: Ensure proper file system permissions
4. **Connection issues**: Verify Claude Desktop configuration

### Debug Mode

Enable debug logging by setting:
```bash
LOG_LEVEL=debug npm start
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Code Style

This project uses:
- ESLint for linting
- Prettier for code formatting
- TypeScript for type safety

## License

MIT License - see LICENSE file for details.

## Resources

- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [Claude Desktop MCP Guide](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
- [TypeScript MCP SDK](https://github.com/modelcontextprotocol/typescript-sdk)

## Changelog

### v1.0.0
- Initial implementation
- Basic tools, resources, and prompts
- TypeScript support
- Error handling and logging
