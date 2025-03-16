FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variable for OpenAI API key
ENV OPENAI_API_KEY=""

# Command to run the Python script
CMD ["python", "my_project/main.py"]