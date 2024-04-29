# Use the official Python image as a base
FROM python:3.12-slim

# Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc

# Install poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock files into the container
COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry install

# Copy the src into the working directory
COPY . .
EXPOSE 8000
# Command to run your application
CMD ["poetry", "run", "python", "src/car_price_prediction/fastapi_application.py"]
