# Use official Python image as base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy all application files (including Schema.py and other helper files)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
