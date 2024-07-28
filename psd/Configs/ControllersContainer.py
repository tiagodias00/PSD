import sys
from typing import Container
from dependency_injector import providers, containers
from InterfaceAdapters.Controllers.APIStatusController import APIStatusController
from InterfaceAdapters.Controllers.SentimentController import SentimentController

class Controllers(containers.DeclarativeContainer):
    modelController = providers.Factory(SentimentController)
    statusController = providers.Factory(APIStatusController)
    print("--- Controllers Dependencies set ---")
    # other controllers