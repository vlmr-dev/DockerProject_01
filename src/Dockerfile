# Set the base image
FROM docker:24.0.6-dind

# Set the image maintainer
LABEL version="1.0.0" description="Python project" maintainer="v1mr<vlmr@email.com>"

# Instalar Python e Flask
RUN apk add --no-cache python3 py3-pip

# Set the location where the app will reside on the container's filesystem
WORKDIR /app

# Copy the requirements
COPY . /app

# Run pip and install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Start
CMD ["python3", "app.py"]