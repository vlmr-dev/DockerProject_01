# Set the base image
FROM postgres:14-alpine

# Set the directory where initialization scripts can be added
COPY . /docker-entrypoint-initdb.d/

# Default port
EXPOSE 5432