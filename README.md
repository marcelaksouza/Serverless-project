## Project

This is a serverless application to help me to refress and learn the following:
- Python
- FastAPI 
- GraphQL
- Graphene
- DynamoDB
- Docker
- Serverless
- Terraform

## Usage
```python
# To run run on docker
docker-compose up --build

# To run locally
cd Serverless-project 
uvicorn main:app --reload --port 5000 

# Or 
cd Serverless-project 
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
