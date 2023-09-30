# Use an official Python runtime as a base image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir Flask transformers torch

# Make port 5002 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask to run in production mode
#ENV FLASK_ENV=production
ENV FLASK_ENV=development

# Run app.py when the container launches - with auto-reloading enabled.
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]
