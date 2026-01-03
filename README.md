# LLM_langgraph: Multi-Agent AI Systems with LangGraph

## 🏗️ Project Overview

LLM_langgraph is a comprehensive implementation of advanced Large Language Model (LLM) applications using the LangGraph framework. This repository provides practical examples of AI agent systems, from basic conversational interfaces to sophisticated multi-agent architectures with supervisor coordination and external tool integration.

## 📁 Repository Structure

```
LLM_langgraph/
│
├── basic_chatbot/              # Foundational single-agent chatbot implementation
│   ├── chain.py                # Core conversation chain implementation
│   ├── graph.py                # LangGraph state machine definition
│   └── app.ipynb               # Interactive notebook demonstration
│
├── Agents/                     # Multi-agent system components
│   ├── researcher.py           # Research specialist agent
│   ├── writer.py               # Content creation agent
│   ├── coder.py                # Code generation agent
│   ├── critic.py               # Quality evaluation agent
│   └── supervisor.py           # Task orchestration agent
│
├── Debugging/                  # Workflow debugging utilities
│   ├── tracer.py               # Execution tracing module
│   ├── visualizer.py           # Graph visualization tools
│   └── state_inspector.ipynb  # State examination notebook
│
├── mcp_demo/                   # Model Context Protocol integration
│   ├── server.py               # MCP server implementation
│   ├── clients/                # Client implementations
│   └── tools/                  # External tool definitions
│
├── requirements.txt            # Project dependencies
└── .gitignore                  # Version control exclusion rules
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10 or higher
- GROQ API key or compatible LLM provider access
- Git version control system

### Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/bitmos/LLM_langgraph.git
cd LLM_langgraph
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

## 🏗️ Architecture

### Multi-Agent System Design

The repository implements an agent architecture where specialized agents collaborate under supervisor coordination.

## 🔧 Core Components

### 1. Basic Chatbot (`basic_chatbot/`)

The foundational implementation demonstrates LangGraph's state management for conversational AI.

**Key Features:**
- Memory-preserving conversation chains
- Streaming response generation
- Customizable prompt templates

### 2. Multi-Agent System (`Agents/`)

A production-ready multi-agent framework with specialized role definitions.

**Agent Definitions:**
- **Researcher Agent**: Performs web search and information synthesis
- **Writer Agent**: Creates structured documents and reports
- **Analyzer Agent**: Evaluates key insights, patterns, risks and opportunities
- **Supervisor Agent**: Orchestrates task execution across specialists

### 3. Debugging Tools (`Debugging/`)

Comprehensive utilities for monitoring and troubleshooting agent workflows.

**Tools Included:**
- Execution tracing with step-by-step logging
- Graph visualization for workflow inspection
- State examination for debugging complex interactions

### 4. MCP Integration (`mcp_demo/`)

Model Context Protocol implementation for extending agent capabilities with external tools.

## 🔍 Advanced Features

### State Management

LangGraph's state graphs maintain context across agent interactions, ensuring coherent multi-step workflows.

### Tool Calling

Agents utilize function-calling capabilities to interact with external systems and execute precise operations.

### Conditional Routing

The supervisor implements intelligent routing logic to direct tasks to the most appropriate specialist agent.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy Building with LangGraph! 🚀**
