from typing import List
from pydantic.dataclasses import dataclass

@dataclass
class TweetDTO:
    
    tweet: str
    entities: list

    def __init__(self, tweet, entities):
        self.tweet = tweet
        self.entities = entities