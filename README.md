# Real-time-Joke-Dashboard-updates
# Django with Celery and Redis - Scheduled Joke Fetching

## Description

This project is a Django-based application that uses Celery and Redis to schedule and process tasks. The main functionality of the project is to fetch jokes periodically using Celery Beat, which schedules tasks at specified intervals. Redis is configured as the message broker to queue tasks, which are then processed by Celery workers. 

## Features
- **Periodic Task Scheduling:** Celery Beat is used to schedule the fetching of jokes every few seconds.
- **Task Processing:** Celery workers process the scheduled tasks and execute them as per the defined logic.
- **Dockerized Environment:** The project is containerized using Docker, making it easy to set up and run in any environment.
- **Redis as Message Broker:** Redis is used to manage the message queue between Django, Celery, and the Celery workers.

## Project Setup

### Prerequisites
- Docker installed on your machine.
- Python 3.9 or later.
- Redis (configured via Docker in this project).

### Local Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nayeemabee/Real-time-Joke-Dashboard-updates.git
   cd .\CeleryProject\
2. **Build Docker image**
    docker-compose up --build
4. **Access the Application**
    navigating to http://localhost:8090 in your web browser.
