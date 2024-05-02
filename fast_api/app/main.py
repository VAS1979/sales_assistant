"""Module main"""

from fastapi import FastAPI

app = FastAPI(
    title="Sales_assistent"
)


@app.get("/")
def get_status():
    """Возвращает статус"""
    return "FastAPI is running"
