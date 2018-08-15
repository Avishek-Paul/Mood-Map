import tweepy
from moodmap import MoodMap

class StreamHandler(tweepy.StreamListener):
    moodmap = MoodMap()
    
    def on_status(self, status):
        self.moodmap.reset_curr()
        self.moodmap.write_log_csv()
        self.moodmap.filter_logic(status.text.lower())

    def on_error(self, status_code):
        if status_code == 420:
            return False 