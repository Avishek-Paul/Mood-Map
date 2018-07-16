import json
import requests
import urllib.parse 
import oauth2 as oauth
import tweepy
from moodmap import MoodMap
from conf.settings import API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET

class StreamHandler(tweepy.StreamListener):
    saved_tweets_location = None
    moodmap = MoodMap()
    
    def on_status(self, status):
        self.moodmap.filter_logic(status.text.lower())
        self.moodmap.print_values()

    def on_error(self, status_code):
        if status_code == 420:
            return False

class PyTweet(object):
    """Functions to access twitter api"""

    def __init__(self):
        self.consumer = oauth.Consumer(key=API_KEY, secret=API_SECRET)
        self.access_token = oauth.Token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)    
        self.client = oauth.Client(self.consumer, self.access_token)

    def api_call(self, method, endpoint, query):
        url = endpoint + urllib.parse.urlencode(query)        
        response, data = self.client.request(uri=url,method=method)
        return response, data

    def get_home_timeline(self,count=20):
        endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json?"
        query = {
            'count': count
        }
        response, data = self.api_call(
            method = 'GET',
            endpoint = endpoint,
            query = query
        )
        print("Status:",response.status)
        return json.loads(data)

    def get_user_timeline(self,screen_name='twitter',count=20):
        endpoint = 'https://api.twitter.com/1.1/statuses/user_timeline.json?'
        query = {
            'screen_name': screen_name,
            'count': count
        }
        response, data = self.api_call(
            method = 'GET',
            endpoint = endpoint,
            query = query
        )
        print("Status:",response.status)
        return json.loads(data)

    def post_status(self,status):
        endpoint = 'https://api.twitter.com/1.1/statuses/update.json?'
        query = {
            'status': status
        }
        response, data = self.api_call(
            method = 'POST',
            endpoint = endpoint,
            query = query
        )
        print("Status:",response.status)
        return json.loads(data)

    def setup_stream(self):
        tweepy_auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
        tweepy_auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        self.stream_api = tweepy.API(tweepy_auth)

    def stream(self,track,locations=None,languages=None,saved_tweets_location=None):
        self.setup_stream()
        stream_handler = StreamHandler()
        stream_handler.saved_tweets_location = saved_tweets_location
        stream = tweepy.Stream(auth=self.stream_api.auth, listener=stream_handler)
        stream.filter(track=track,languages=languages,locations=locations)
