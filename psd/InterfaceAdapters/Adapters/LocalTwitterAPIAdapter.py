from dataclasses import asdict
import requests
from ApplicationServices.IAdapters.ILocalTwitterAdapter import ILocalTwitterAdapter
from Utils.FileImporter import FileImporter

class LocalTwitterAPIAdapter(ILocalTwitterAdapter):

    database = FileImporter.load_json_database()

    def get_tweets(self, entity: str):
        tweets_to_analyse = []
        for row in self.database.itertuples(index=False):
            tweet = str(row.text)
            if tweet != None and entity in tweet:
                tweets_to_analyse.append(tweet)

        return tweets_to_analyse        