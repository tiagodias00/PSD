from typing import List
from pydantic.dataclasses import dataclass

from DTOs.TweetDTO import TweetDTO

@dataclass
class AnalysisDTO:
    
    num_positive_sentiments: int
    num_negative_sentiments: int
    num_neutral_sentiments: int
    lst_positive_tweets: list
    lst_negative_tweets: list
    lst_neutral_tweets: list


    def __init__(self, num_positive_sentiments, num_negative_sentiments, num_neutral_sentiments, lst_positive_tweets, lst_negative_tweets, lst_neutral_tweets):
        self.num_positive_sentiments = num_positive_sentiments
        self.num_negative_sentiments = num_negative_sentiments
        self.num_neutral_sentiments = num_neutral_sentiments
        self.lst_positive_tweets = lst_positive_tweets
        self.lst_negative_tweets = lst_negative_tweets
        self.lst_neutral_tweets = lst_neutral_tweets
