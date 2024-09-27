# Microservices FastAPI Backend Base

### This repository will be used as the base for the microservice architecture backend for the mock interview project.

## Architecture

- `app`: Responsible for handling the FastAPI application.
  - `database`: Responsible for handling the database operations.
    - `models`: Responsible for handling the database models.
    - `repository`: Responsible for handling the database operations for a specific entity.
  - `services`: Responsible for handling the business logic.
  - `routes`: Responsible for handling the API routes.
  - `utils`: Responsible for handling the utility functions.
  - `types`: Responsible for handling the type definitions for request and response payloads and broker messages.
  - `dependencies.py`: Responsible for handling the dependencies and middlewares.

### Broker

In the `services` directory, there is a `broker` directory that is responsible for handling the communication between the services. The broker is divided into two parts:

- `events`: Responsible for handling the events between the services.
- `rpc`: Responsible for handling the Remote Procedure Calls (RPC) between the services.

## Setup

1. Clone the repository.

2. Create a virtual environment.

```bash
python3 -m venv .venv
```

3. Activate the virtual environment.

```bash
source .venv/bin/activate # Linux or macOS
.venv\Scripts\activate # Windows
```

4. Install the dependencies.

```bash
pip install -r requirements.txt
```

5. Start the docker containers.

```bash
docker-compose up -d
```

6. Setup the environment variables in the `.env` file.

7. Run the FastAPI application.

```bash
python3 -m app
```
