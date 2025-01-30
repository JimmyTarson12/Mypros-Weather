FROM python:3.12-alpine

WORKDIR /app

# Get requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

# Copy file
COPY weather.py .

# Get coordinates
ENV LATITUDE=40.7128
ENV LONGITUDE=-74.0060

ENTRYPOINT ["python", "weather.py"]
