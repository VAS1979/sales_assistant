"""
Модуль main приложения fast_api
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI

from .services.request_handler import loading_data


app = FastAPI(
    title="Sales_assistent"
)


@app.get("/")
def get_status():
    """
    Возвращает статус приложения.
    """
    return "FastAPI is running"


@app.get("/response")
def get_parser_response():
    """
    Возвращает ответ парсера.
    """
    return loading_data()
