import os
import time
import tweepy
import pandas as pd
from conf.settings import all_words, update_time, log_path, log_name

class MoodMap(object):
    """Logic for the collection of tweets"""
    def __init__(self):
        self.last_update = time.time()

        self.total_count = {
            'happy': 0,
            'sad': 0,
            'angry': 0,
            'fear': 0
        }

        self.current_count = {
            'happy': 0,
            'sad': 0,
            'angry': 0,
            'fear': 0
        }

        self.happy_words = all_words['happy_words']
        self.sad_words = all_words['sad_words']
        self.angry_words = all_words['angry_words']
        self.fear_words = all_words['fear_words']

    def reset_curr(self):
        if time.time() - self.last_update > update_time:
            self.current_count = {emotion: 0  for emotion in self.current_count}
            self.last_update = time.time()
        
    def filter_logic(self,text):
        
        if any(x in text for x in self.happy_words):
            self.total_count['happy']+=1
            self.current_count['happy']+=1
        if any(x in text for x in self.sad_words):
            self.total_count['sad']+=1
            self.current_count['sad']+=1
        if any(x in text for x in self.angry_words):
            self.total_count['angry']+=1
            self.current_count['angry']+=1
        if any(x in text for x in self.fear_words):
            self.total_count['fear']+=1
            self.current_count['fear']+=1

    def write_log_csv(self):
        tdf = pd.DataFrame.from_dict(self.total_count, orient='index')
        cdf = pd.DataFrame.from_dict(self.current_count, orient='index')
        df = tdf.join(cdf, lsuffix='total', rsuffix='current')
        df.columns = ['total', 'current']
        df.to_csv(log_path + log_name, index=False)