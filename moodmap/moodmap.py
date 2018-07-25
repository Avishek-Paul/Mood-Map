import os
import time
import tweepy
from conf.settings import all_words, update_time, log_path

class MoodMap(object):
    """Logic for the collection of tweets"""
    def __init__(self):
        self.last_update = time.time()

        self.total_happy_count = 0
        self.total_sad_count = 0
        self.total_angry_count = 0
        self.total_fear_count = 0

        self.curr_happy_count = 0
        self.curr_sad_count = 0
        self.curr_angry_count = 0
        self.curr_fear_count = 0

        self.happy_words = all_words['happy_words']
        self.sad_words = all_words['sad_words']
        self.angry_words = all_words['angry_words']
        self.fear_words = all_words['fear_words']

    def reset_curr(self):
        if time.time() - self.last_update > update_time:
    
            self.curr_happy_count = 0
            self.curr_sad_count = 0
            self.curr_angry_count = 0
            self.curr_fear_count = 0
                
            self.last_update = time.time()

            return True

        else:
            
            return False
        
    def filter_logic(self,text):
        
        if any(x in text for x in self.happy_words):
            self.total_happy_count+=1
            self.curr_happy_count+=1
        if any(x in text for x in self.sad_words):
            self.total_sad_count+=1
            self.curr_sad_count+=1
        if any(x in text for x in self.angry_words):
            self.total_angry_count+=1
            self.curr_angry_count+=1
        if any(x in text for x in self.fear_words):
            self.total_fear_count+=1
            self.curr_fear_count+=1
            
    def get_curr_values(self):
        values = "Happy: {}\n Sad: {}\n Angry: {}\n Scared: {}\n"
        values = values.format(
                    self.curr_happy_count,
                    self.curr_sad_count,
                    self.curr_angry_count,
                    self.curr_fear_count)
        return values

    def get_total_values(self):
        values = "Happy: {}\n Sad: {}\n Angry: {}\n Scared: {}\n"
        values = values.format(self.total_happy_count,
                    self.total_sad_count,
                    self.total_angry_count,
                    self.total_fear_count)
        return values

    def write_log(self):

        if not os.path.exists(log_path):
            os.mkdir(log_path)

        filename = 'total_values.txt'

        log = open(log_path+filename, 'w+')
        log.write(self.get_total_values())
        log.close()