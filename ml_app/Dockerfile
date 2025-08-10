# /home/testuser/Linux-Infrastructure-Automation-Lab/ml_app/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies, including gunicorn and Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port on which the app will run
EXPOSE 5000

# Command to run the application using Gunicorn
# "app:app" means: module 'app' (app.py) and app instance 'app'
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
