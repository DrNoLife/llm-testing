# Use an official Python runtime as a base image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir transformers torch

# Open a bash session when the container starts
CMD ["/bin/bash"]
