FROM python:3.12-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python script
COPY weather.py .

# Environment variables (Defualt new york)
ENV LATITUDE=40.7128
ENV LONGITUDE=-74.0060

# Set the entrypoint to run the script with parameters
ENTRYPOINT ["python", "weather.py"]
