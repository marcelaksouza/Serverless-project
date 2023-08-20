import graphene
import uvicorn
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler #,make_graphiql_handler

from server.utils.db import Initialize_db
from server.utils.seeds import add_seeds

app = FastAPI(title='ServerlessAP', description='GraphQL APIs', version='0.1')

# Db initializing 
ddb = Initialize_db()
#To populate DB with seeds
add_seeds(ddb) 

# testing api basic Hello World
@app.get("/")
async def root():
    return {"message": "Hello World"}

# testing graphql
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return "Hello " + name

schema = graphene.Schema(query=Query)


# app.mount("/", GraphQLApp(schema, on_get=make_graphiql_handler()))  # Graphiql IDE
app.mount("/graphql", GraphQLApp(schema, on_get=make_playground_handler()))  # Playground IDE
# app.mount("/", GraphQLApp(schema)) # no IDE

if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)

