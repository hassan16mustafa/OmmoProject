# Use an official Python image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the project
CMD ["python", "main.py", "input_folder", "output_folder"]
