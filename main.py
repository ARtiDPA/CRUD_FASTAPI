from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main_root():
    return {'message': 'project for FastAPI and Posgresql'}