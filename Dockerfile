# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Install pipx for managing poetry or pip-tools
RUN pip install --upgrade pip

# Copy the requirements.txt file
COPY requirements.txt ./

# Install dependencies using poetry
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["python", "app.py"]