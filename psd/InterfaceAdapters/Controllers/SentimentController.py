from dataclasses import asdict
from InterfaceAdapters.IControllers.ISentimentController import ISentimentController

from fastapi import APIRouter
from starlette.responses import JSONResponse
from DTOs.AnalysisDTO import AnalysisDTO
from Configs.ServiceContainers import Services

class SentimentController(ISentimentController):
    
    router = APIRouter()
    
    @router.post("/analyze", response_model=AnalysisDTO, tags=["sentiment"])
    async def analyze_sentiment(entity: str):
        analysis: AnalysisDTO = Services.sentimentAnalysis().analyze_sentiment(entity)
        return JSONResponse(asdict(analysis))
