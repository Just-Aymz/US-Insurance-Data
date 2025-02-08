<<<<<<< HEAD
# Use official Python base image
FROM python:3.9-slim
=======
# Use official Python image as base
FROM python:3.9
>>>>>>> d85bb04f61c87ee9ae7d5372c1caa56a7b4504d7

# Set the working directory in the container
WORKDIR /app

<<<<<<< HEAD
# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app and other necessary files into the container
COPY . .

# Expose the port the app will run on
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
# Copy all application files (including Schema.py and other helper files)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> d85bb04f61c87ee9ae7d5372c1caa56a7b4504d7
