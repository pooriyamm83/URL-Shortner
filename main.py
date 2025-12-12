from fastapi import FastAPI
from url_shortner.routers.url_router import router
# if done bonus part add : from commands.cleanup import scheduler

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "URL Shortener API is running!"}