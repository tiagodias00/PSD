from sqlite3 import adapters

import torch
from ApplicationServices.IAdapters.ILocalTwitterAdapter import ILocalTwitterAdapter
from ApplicationServices.IDataProcessors.IDataProcessor import IDataProcessor
from ApplicationServices.Services.IAppServices.ISentimentAnalysisService import ISentimentAnalysisService
from Configs.DataProcessorsContainer import DataProcessors
from Configs.AdaptersContainer import Adapters
from ApplicationServices.IMLModels.IMLModel import IMLModel
from Configs.MLModelsContainer import MLModels
from pysentimiento import preprocessing
from DTOs.AnalysisDTO import AnalysisDTO
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForTokenClassification
from transformers import pipeline

from DTOs.TweetDTO import TweetDTO

class SentimentAnalysisService(ISentimentAnalysisService):

    tokenizer = AutoTokenizer.from_pretrained("pysentimiento/robertuito-sentiment-analysis")
    model = AutoModelForSequenceClassification.from_pretrained("pysentimiento/robertuito-sentiment-analysis")
    ner_tokenizer = AutoTokenizer.from_pretrained("pysentimiento/robertuito-ner")
    ner_model = AutoModelForTokenClassification.from_pretrained("pysentimiento/robertuito-ner")
    ner = pipeline("ner", model=ner_model, tokenizer=ner_tokenizer)
    data_processor: IDataProcessor = DataProcessors.textDataProcessor()
    adapter: ILocalTwitterAdapter = Adapters.twitterAdapter()

    def analyze_sentiment(self, entity: str):
        # query the entity in twitter stream database
        tweets = self.adapter.get_tweets(entity)

        # run sentiment analysis for each tweet
        pos_tweets = []
        neg_tweets = []
        neu_tweets = []
        for tweet in tweets:
            preprocessed_tweet = preprocessing.preprocess_tweet(tweet, lang="en")
            inputs = self.tokenizer(preprocessed_tweet, return_tensors="pt")
            outputs = self.model(**inputs)
            output = self._get_output(outputs.logits)
            pred = "NEG"
            if(output["NEU"] > output[pred]):
                pred = "NEU"
            if(output["POS"] > output[pred]):
                pred = "POS"

            # perform Entity recognition (V1)
            entities = self.predict_ner(preprocessed_tweet)

            entities_str = ""
            for entity in entities:
                entities_str += entity["text"] + ";" + entity["type"] + "|"

            if(pred == "POS"):
                pos_tweets.append(tweet + " Entities: " + entities_str)
            elif(pred == "NEG"):
                neg_tweets.append(tweet + " Entities: " + entities_str)
            else:
                neu_tweets.append(tweet + " Entities: " + entities_str)
                
        # perform Key Entity recognition (V2)

        # return the predictions to the user
        return AnalysisDTO(len(pos_tweets), len(neg_tweets), len(neu_tweets), pos_tweets, neg_tweets, neu_tweets)



    def _get_output(self, logits):
        """
        Get output from logits
        It takes care of the type of problem: single or multi label classification
        """
        probs = torch.sigmoid(logits).view(-1)
        probas = {self.model.config.id2label[i]:probs[i].item() for i in self.model.config.id2label}
        return probas

    def predict_ner(self, inputs):
        """
        Predict token classification
        """
        if isinstance(inputs, str):
            inputs = [inputs]

        ret = self.ner(inputs, aggregation_strategy="simple")

        for sent, entities in zip(inputs, ret):
            for entity in entities:
                start, end = entity["start"], entity["end"]
                entity["text"] = sent[start:end].strip()
                entity["type"] = entity.pop("entity_group")

        if len(inputs) == 1:
            return ret[0]
        return ret