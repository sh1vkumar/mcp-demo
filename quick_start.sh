#!/bin/bash

# Claude Efficiency Tools - Quick Start Script
# This script helps you get started with the MCP server

set -e

echo "🚀 Claude Efficiency Tools - Quick Start"
echo "========================================"
echo ""

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ Error: uv is not installed."
    echo "Please install uv first: https://docs.astral.sh/uv/getting-started/installation/"
    exit 1
fi

echo "✅ uv is installed"

# Check if we're in the right directory
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found in current directory"
    echo "Please run this script from the project root directory"
    exit 1
fi

echo "✅ Project files found"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
uv sync

echo "✅ Dependencies installed"

# Test the server
echo ""
echo "🧪 Testing the MCP server..."
echo "Testing server import..."

# Test that the server can be imported
if uv run python -c "from main import mcp; print('✅ Server imports successfully')" 2>/dev/null; then
    echo "✅ Server imports successfully"
else
    echo "❌ Failed to import server"
    exit 1
fi

echo "✅ Server test completed"

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Copy the configuration from claude_desktop_config.json to your Claude Desktop config"
echo "2. Restart Claude Desktop"
echo "3. Start using the efficiency tools!"
echo ""
echo "📁 Claude Desktop config locations:"
echo "   macOS: ~/Library/Application Support/Claude/claude_desktop_config.json"
echo "   Windows: %APPDATA%/Claude/claude_desktop_config.json"
echo "   Linux: ~/.config/Claude/claude_desktop_config.json"
echo ""
echo "🔧 To start the server manually:"
echo "   uv run server main stdio"
echo ""
echo "📖 For more information, see README.md"
