FROM python:3.9-slim

# Create necessary directories inside the container
RUN mkdir -p /app

WORKDIR /app

# Copy all files from the current directory (build context) into the /app directory in the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the necessary ports
EXPOSE 8000 8501

# Default command (overridden by docker-compose)
CMD ["sh", "-c", "echo 'Use docker-compose to run FastAPI and Streamlit as separate services.'"]
