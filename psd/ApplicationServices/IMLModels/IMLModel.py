import abc

class IMLModel(abc.ABC):

    @abc.abstractmethod
    def predict(self, evidences):
        pass