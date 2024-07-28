from InterfaceAdapters.Adapters.LocalTwitterAPIAdapter import LocalTwitterAPIAdapter
from typing import Container
from dependency_injector import providers, containers

class Adapters(containers.DeclarativeContainer):
    twitterAdapter = providers.Factory(LocalTwitterAPIAdapter)
    print("--- Adapters Dependencies set ---")
    # other controllers