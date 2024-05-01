"""Module main"""

from fastapi import FastAPI

print("FastAPI is running")

app = FastAPI()


@app.get("/")
def get_status():
    """Возвращает статус"""
    return "FastAPI is running"
