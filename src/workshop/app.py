import uvicorn
from fastapi import FastAPI

from workshop.api import router

app = FastAPI()
app.include_router(router)

@app.get('/')
def root():
    return {'message': 'Hi'}

