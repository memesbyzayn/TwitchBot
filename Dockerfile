# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PORT=5000

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire application code into the container
COPY . /app/

# Expose the port Railway will use (Railway sets PORT via environment variable)
EXPOSE $PORT

# Command to run your app (adjust the filename if needed)
CMD ["python", "flask_twitch_webapp2.py"]
