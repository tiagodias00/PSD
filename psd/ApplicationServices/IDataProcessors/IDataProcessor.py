import abc

from numpy import ndarray

class IDataProcessor(abc.ABC):

    @abc.abstractmethod
    def preprocess_text_data(self, text) -> list:
        pass