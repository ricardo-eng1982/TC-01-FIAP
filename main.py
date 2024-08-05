from fastapi import FastAPI
import requests

app = FastAPI()
#Rota teste
@app.get("/")
async  def get_teste():
    return {"message": "API OK"}
# Rota para documentação OpenAPI
@app.get("/docs")
async def get_docs():
    return {"message": "Acesse /docs para a documentação OpenAPI"}

# Rota para documentação Redoc
@app.get("/redoc")
async def get_redoc():
    return {"message": "Acesse /redoc para a documentação Redoc"}
