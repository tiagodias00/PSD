from InterfaceAdapters.IControllers.IAPIStatusController import IAPIStatusController
from typing import Container
from fastapi import APIRouter, Body, Depends
from starlette import status

class APIStatusController(IAPIStatusController):
    
    router = APIRouter()

    @router.get("/")
    async def status() -> str:
        return {"status" : "🛡️ Welcome to the Public Sentiment Detector API 🛡️"}
