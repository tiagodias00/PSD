from dependency_injector import providers, containers
from InterfaceAdapters.DataProcessors.TextDataProcessor import TextDataProcessor

class DataProcessors(containers.DeclarativeContainer):
    textDataProcessor = providers.Factory(TextDataProcessor)
    print("--- Data Processors Dependencies set ---")
    # other data processors