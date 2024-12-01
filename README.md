# Project Setup Guide

This guide will walk you through the steps to set up and run the project on your local system.

## Prerequisites

Before you begin, ensure that you have the following installed on your machine:

1. **Python 3.x** (Recommended: Python 3.8+)
2. **Docker** 
3. **RabbitMQ** (or install via Docker)
4. **Git**

## Setup Steps

### 1. Clone the Repository
Start by cloning the repository to your local machine:

```bash
git clone https://github.com/devbrat882jha/task_iot_mmqtt.git

**2. Create a Virtual Environment**

    python -m venv env

**3. Install the Required Python Dependencies**

    pip install -r requirements.txt

**4. Install RabbitMQ**

**5. Pull the Latest MongoDB Docker Image**

     docker pull mongo:latest

**6. Run MongoDB in Docker Container**

     docker run -d --name mongodb-container -p 27017:27017 mongo:latest

**7. Run the RabbitMQ Client**

     cd app/
     python mq_tt_client.py

**8. Run the RabbitMQ Consumer**

     python rabbitmq_consumer.py

**9. Start the FastAPI Application**
     uvicorn main.app --reload
     The FastAPI application will be running at http://localhost:8000.
     Access apis at http://localhost:8000/docs





