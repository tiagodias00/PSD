from abc import ABC
import abc

class ISentimentController(abc.ABC):

    @abc.abstractmethod
    def analyze_sentiment(self, numericEvidences: list, categoricalEvidences:list) -> list:
        pass