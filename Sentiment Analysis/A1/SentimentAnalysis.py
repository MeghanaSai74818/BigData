import json
import configparser
import tweepy
from kafka import KafkaProducer
from transformers import pipeline
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener



def classifyTweet(single_tweet):
    return ((classifier(json.loads(single_tweet)["text"]))[0]['label'])

class KafkaListener(StreamListener):
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers = ['localhost:9092'])

    
    def on_data(self, data):
        sentiment = classifyTweet(data)
        self.producer.send(config['arguments']['topic'], bytes(sentiment, encoding = 'utf-8'))
        return True
    
    def on_error(self, status):
        print("Error fetching tweet from Twitter with the status error as: ", status)
        return True


API_consumer_key = "E09csWbvA02pwatuxqDAYHABk"
API_consumer_secret = "ouchHC7Srd8N6oNBZbNhyIDpUsAm0cNN4s50NXLlSqvCVXGkDT"
API_access_token = "1515463742468902922-XotACFybidHHtSwnOAdDsDYy1T1Azx"
API_access_secret = "0rtVpif43x06wT6QWhZ70CjZHW3ltzinkqRdhouqKShIV"



if __name__ == "__main__": 
    auth = OAuthHandler(API_consumer_key, API_consumer_secret)
    auth.set_access_token(API_access_token, API_access_secret)
    api = tweepy.API(auth)
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    classifier = pipeline('sentiment-analysis')
    
    listener = KafkaListener()
    unfilteredData = Stream(auth, listener)
    unfilteredData.filter(track=[config['arguments']['hashtag']])
