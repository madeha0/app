
# Use an official Python base image
FROM python:3.11-slim

# Create a non-root user
RUN useradd -m appuser

# Set the working directory
WORKDIR /app

# Install required system packages
RUN apt-get update && apt-get install -y \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgl1 \
    libglib2.0-0 \
    cmake \
    build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create the downloads directory and set permissions
RUN mkdir -p /app/downloads && chown appuser:appuser /app/downloads

# Add local bin to PATH for appuser
ENV PATH="/home/appuser/.local/bin:$PATH"

# Switch to the non-root user
USER appuser

# Copy application files
COPY --chown=appuser:appuser requirements.txt requirements.txt
COPY --chown=appuser:appuser Wheels/ Wheels/
COPY --chown=appuser:appuser . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the app
CMD ["sh", "-c", "python download_file.py && python app/app.py"]
