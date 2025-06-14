# Use official lightweight base image
FROM python:3.10-slim

# Set working directory first
WORKDIR /app

# Install system dependencies in one layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libportaudio2 \
    portaudio19-dev \
    gcc \
    libc-dev \
    make \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code (this layer will only rebuild if code changes)
COPY . .

# Create uploads directory if needed
RUN mkdir -p uploads

# Set environment variables
ENV PYTHONPATH=/app
ENV GRADIO_SERVER_NAME=0.0.0.0
ENV GRADIO_SERVER_PORT=7860

# Expose the required port
EXPOSE 7860

# Start the application (simplified command)
CMD ["python", "gradio_app.py"]