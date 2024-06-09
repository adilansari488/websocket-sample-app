# Use the Python 3.10 slim base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python app files to the working directory
COPY *.py .

# Set the entrypoint command to run the Python app
CMD ["python", "server.py"]