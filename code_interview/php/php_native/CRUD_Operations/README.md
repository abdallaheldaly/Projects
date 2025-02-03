# Task Manager Application

A simple CRUD (Create, Read, Update, Delete) task management system built with PHP, Nginx, and Docker.

![Task Manager Demo](https://via.placeholder.com/800x400.png?text=Task+Manager+Interface)

## Features

- 🚀 **Create Tasks**: Add new tasks instantly
- ✏️ **Edit Tasks**: Modify existing tasks
- 🗑️ **Delete Tasks**: Remove unwanted tasks
- 💾 **Persistent Storage**: JSON file-based data storage
- 🐳 **Dockerized Environment**: Easy container setup

## Technologies Used

- PHP 8.2
- Nginx
- Docker
- Docker Compose

## Prerequisites

- Docker Engine ≥ 20.10
- Docker Compose ≥ 2.17

## Installation

1. **Clone the repository** (if applicable):
    mkdir -p {nginx,src,data}
    touch data/tasks.json

    chmod 777 data

# ▶️ Start application:
docker-compose up -d


# ⏹️ Stop application:
docker-compose stop

# ♻️ Rebuild containers:
docker-compose up -d --build

# 🛑 Remove containers:
docker-compose down



