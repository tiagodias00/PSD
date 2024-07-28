import sys
from typing import Container
from dependency_injector import providers, containers
from ApplicationServices.Services.AppServices.SentimentAnalysisService import SentimentAnalysisService

#from ADE.InterfaceAdapters.Adapters import RuleGeneratorAdapter

class Services(containers.DeclarativeContainer):
    sentimentAnalysis = providers.Factory(SentimentAnalysisService)
    print("--- Services Dependencies set ---")
    # other services