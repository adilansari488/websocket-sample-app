# Use the Python 3.10 slim base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python dependencies file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt --no-cache-dir

# Copy the Python app files to the working directory
COPY *.py .

# Set the entrypoint command to run the Python app
CMD ["python", "server.py"]