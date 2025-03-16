# Setup Instructions for KB-agents-ui

This project demonstrates the OpenAI Agents SDK with both a Python backend and Svelte frontend. Follow these steps to set up and run the project:

## Requirements
- Python 3.7 or later
- Node.js 14 or later (for the frontend)
- An OpenAI API key

## Backend Setup (Python)

1. Create a virtual environment:
   ```sh
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key:
   ```sh
   export OPENAI_API_KEY="your-api-key-here"
   ```

5. Run the backend:
   ```sh
   python my_project/main.py
   ```

## Frontend Setup (Svelte)

1. Navigate to the svelte-project directory:
   ```sh
   cd svelte-project
   ```

2. Install dependencies:
   ```sh
   npm install
   ```

3. Run the development server:
   ```sh
   npm run dev
   ```

4. Open your browser and navigate to http://localhost:3000

## Tkinter UI (Alternative)

For a simple GUI using Tkinter, run:
```sh
python ui/app.py
```

## Testing

Run tests with:
```sh
python -m pytest tests/
```

Note: The Svelte project is set up but requires the missing component files to be created based on the App.svelte imports.