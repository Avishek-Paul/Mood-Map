import tweepy
from moodmap import MoodMap

class StreamHandler(tweepy.StreamListener):
    saved_tweets_location = None
    moodmap = MoodMap()
    
    def on_status(self, status):
        self.moodmap.filter_logic(status.text.lower())
        self.moodmap.print_curr_values()

    def on_error(self, status_code):
        if status_code == 420:
            return False