## URL Shortener API

### Description
This is a simple FastAPI application designed to shorten long URLs into more manageable and shareable links. With this application, users can create short URLs that redirect to their original long URLs.

### Installation
Instructions on how to install and run the project.

### Install Requirements
```bash
pip install -r requirements.txt
```

### Run the Server
```bash
uvicorn app.main:app --reload
```
The API will be accessible at http://localhost:8000.

### How to run with Docker Compose
1. Install Docker 
2. Create .env file
3. Run `docker-compose up -d` in the terminal. The -d flag runs the containers in the background. The services defined in the docker-compose.yml file, such as the FastAPI application and PostgreSQL database, will be built and started. 
4. Access the FastAPI application by navigating to http://localhost:6565 in your web browser.

### Sample .env file format
```dotenv
    ENV=env
    DB=postgresql
    DB_USER=your_user
    DB_PASSWORD=your_password
    DB_HOST=db
    DB_PORT=5432
```

### Integrated with:
1. Python3.11+
2. Fastapi 0.110.0
3. Database: Postgresql
4. Docker 


### References
1. [FastAPI official docs](https://fastapi.tiangolo.com/)
2. [Sqlalchemy official documentation](https://docs.sqlalchemy.org/)
3. [Docker official tutorial](https://docs.docker.com/get-started/)
