# KB Agents UI

A demonstration of the OpenAI Agents SDK with both Python backend and Svelte frontend interfaces. This project showcases how to build agentic AI applications with features like agent delegation, guardrails, and trace monitoring.

## Project Structure

- **my_project/**: Python implementation of the agents
- **ui/**: Simple Tkinter UI for interacting with agents
- **svelte-project/**: Modern web UI built with Svelte and Tailwind CSS
- **tests/**: Test suite for the agent functionality

## Features

- **Agent Orchestration**: Create multiple specialized agents that can collaborate
- **Agent Delegation**: Triage agents can route queries to specialist agents
- **Guardrails**: Input validation to ensure appropriate agent responses
- **Multiple UIs**: Choose between simple Tkinter UI or modern Svelte frontend
- **Tracing**: Monitor agent thought processes and delegation

## Running the Project

Please refer to [SETUP_INSTRUCTIONS.md](./SETUP_INSTRUCTIONS.md) for detailed installation and running instructions.

### Quick Overview

1. **Python Backend**
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   export OPENAI_API_KEY="your-api-key-here"
   python my_project/main.py
   ```

2. **Tkinter UI**
   ```
   python ui/app.py
   ```

3. **Svelte Frontend**
   ```
   cd svelte-project
   npm install
   npm run dev
   ```

## Example Agents

The project includes several agent types:
- Triage Agent: Routes questions to appropriate specialists
- Math Tutor Agent: Answers mathematical questions
- History Tutor Agent: Provides historical information
- Guardrail Agent: Validates that queries are homework-related

## Testing

Run the test suite with:
```
python -m pytest tests/
```

## License

MIT
