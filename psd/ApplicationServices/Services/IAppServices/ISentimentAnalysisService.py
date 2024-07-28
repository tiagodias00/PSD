import abc

class ISentimentAnalysisService(abc.ABC):

    @abc.abstractmethod
    def analyze_sentiment(self, entity: str):
        pass
    