# Pull a base image
FROM python:3.9-slim-buster
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Create a working directory for the django project
WORKDIR /code_elearning
# Copy requirements to the container
COPY Pipfile Pipfile.lock /code_elearning/
# Install the requirements to the container
RUN pip install pipenv && pipenv install --system
# Copy the project files into the working directory
COPY . /code_elearning/
# Open a port on the container
EXPOSE 8000