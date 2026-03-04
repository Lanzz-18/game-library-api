from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"The Video Game Library API is running!"}