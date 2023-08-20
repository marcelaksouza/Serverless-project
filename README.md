## Project: Expenses app

This is a serverless application to help me to refress and learn the following:
- Python 
- FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints  
- GraphQL: GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.
- Graphene: Graphql library supported by FastApi
- DynamoDB: Database
- Docker: Container
- Serverless: 
- Terraform: 

## Usage
```python
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
    - DynamoDB container
        - DB connection
        - Seeds
    - Admin db container
    - Application container
    - Connection between containers
- Add GraphQL
    - Hello word query
    - Add playgound
- Add env variables

## :writing_hand: Todo
- Add Serverless
- CRUD using GraphQL
- Add Unit test
- Add terraform
- Migrate to aws using Terraform 
- Implement CICD
