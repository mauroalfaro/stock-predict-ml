from fastapi import FastAPI


app = FastAPI()


@app.get("/test")
def pong():
    return {"test": "Stock predict is up!"}