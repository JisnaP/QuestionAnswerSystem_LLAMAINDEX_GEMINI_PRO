FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files first
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -U pip setuptools wheel
RUN pip install --no-cache-dir llama-index google-generativeai llama-index-llms-gemini pypdf python-dotenv ipython llama-index-embeddings-gemini streamlit
RUN pip install -e .

# Set environment variables
ENV PORT=8501
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Create necessary directories if they don't exist
RUN mkdir -p logs notebook/storage

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "StreamlitApp.py", "--server.port=8501", "--server.address=0.0.0.0"]
