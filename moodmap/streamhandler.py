import tweepy
from moodmap import MoodMap

class StreamHandler(tweepy.StreamListener):
    saved_tweets_location = None
    moodmap = MoodMap()
    
    def on_status(self, status):
        if self.moodmap.reset_curr() == True:
             self.moodmap.write_log()
        self.moodmap.filter_logic(status.text.lower())

    def on_error(self, status_code):
        if status_code == 420:
            return False 