# Set the base image
FROM python:3.12-slim

# Set the image maintainer
LABEL version="1.0.0" description="Python project" maintainer="v1mr<vlmr@email.com>"

# Set the location where the app will reside on the container's filesystem
WORKDIR /app

# Copy the requirements
COPY . .

# Run pip and install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Internally uses default port
EXPOSE 8000

# Start the API with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]