# File Upload Application

A simple file management application using Docker, Nginx, and PHP Native.

## Features

- File upload functionality
- File listing with timestamps
- File deletion
- Image file validation (JPG, JPEG, PNG, GIF)
- Persistent file storage
- Dockerized environment

## Prerequisites

- Docker
- Docker Compose

## Getting Started

# Create necessary directories
mkdir -p uploads nginx src

# Set permissions for uploads directory (Linux/Mac only)
chmod 777 uploads

# Start the containers
docker-compose up -d

http://localhost:8080


## Stop the Application
docker-compose down

