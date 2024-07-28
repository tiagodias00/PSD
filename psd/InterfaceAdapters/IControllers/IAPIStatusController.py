from abc import ABC
import abc

class IAPIStatusController(abc.ABC):

    @abc.abstractmethod
    def status(self) -> str:
        pass