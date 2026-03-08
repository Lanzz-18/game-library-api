from fastapi import FastAPI
from routes import games

app = FastAPI()
app.include_router(games.router)

@app.get("/")
def read_root():
    return {"message":"The Video Game Library API is running..."}