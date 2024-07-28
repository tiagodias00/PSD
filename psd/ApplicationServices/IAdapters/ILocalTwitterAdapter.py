import abc

class ILocalTwitterAdapter(abc.ABC):

    @abc.abstractmethod
    def get_tweets(self, entity: str) -> any:
        pass