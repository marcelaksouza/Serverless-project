## Project: Expenses app

:arrow_backward: Backend
This is a serverless application to help me to refress and learn the following:
- Python 
- FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints  
- GraphQL: GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.
- Graphene: Graphql library supported by FastApi
- DynamoDB: metaData
- MangoDB: uData
- Docker: Container
- Serverless 
- Terraform

:arrow_forward: Frontend
- React

## Usage
```python
#Start the virtual env
venv\Scripts\activate.bat
# To run run on docker
# DB graphic interface: http://localhost:8001/
# GraphQL playground: http://localhost:5000/graphql/
# Application: http://localhost:5000/
docker-compose up --build


# To run locally 
# first activate the virtual env path/to/venv/Scripts/activate.bat
cd Serverless-project 
uvicorn main:app --reload --port 5000 
# Or 
cd Serverless-project/server 
python main.py

## To run db locally
docker run -p 8000:8000 -d amazon/dynamodb-local
set DYNAMO_ENDPOINT=http://localhost:8000
dynamodb-admin
```

## ✅ Done
- Docker 
    - DynamoDB - metaData container
        - DB connection
        - Seeds
    - Admin DB container
    - React - Client container
    - FastAPI/Uvicorn - Server container
- Add GraphQL
    - Hello word query
    - Add playgound
- Add env variables

## :writing_hand: Todo
- Add Serverless
- CRUD using GraphQL
- Add Unit test
- Add terraform
- Migrate to AWS using Terraform 
- Implement CICD
- Add Udata mangoDB
