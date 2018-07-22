import time

class MoodMap(object):
    """Logic for the collection of tweets"""
    def __init__(self):
        self.last_update = time.time();
        self.total_happy_count = 0
        self.total_sad_count = 0
        self.total_angry_count = 0
        self.total_fear_count = 0
        self.happy_words = ['cheerful', 'contented', 'delighted', 'excited', 'fulfilled', 'glad', 'gleeful', 'gratified', 'happy', 'healthy self-esteem', 'joyful', 'lively', 'merry', 'optimistic', 'playful', 'pleased', 'proud', 'rejuvenated', 'satisfied']
        self.sad_words = ['dejected', 'discouraged', 'dispirited', 'down', 'downtrodden', 'drained', 'forlorn', 'gloomy', 'grieving', 'heavy-hearted', 'melancholy', 'mournful', 'sad', 'sorrowful', 'weepy', 'weary']
        self.angry_words = ['affronted', 'aggravated', 'angry', 'antagonized', 'arrogant', 'bristling', 'exasperated', 'incensed', 'indignant', 'inflamed', 'mad', 'offended', 'resentful', 'riled up', 'sarcastic']
        self.fear_words = ['afraid', 'alarmed', 'anxious', 'aversive', 'distrustful', 'fearful', 'jumpy', 'nervous', 'perturbed', 'rattled', 'shaky', 'startled', 'suspicious', 'unnerved', 'unsettled', 'wary', 'worried']
        
    def filter_logic(self,text):
        
        if time.time() - self.last_update > 15:

            self.total_happy_count = 0;
            self.total_sad_count = 0;
            self.total_angry_count = 0;
            self.total_fear_count = 0;
            self.last_update = time.time();

        else:

            if any(x in text for x in self.happy_words):
                self.total_happy_count+=1
            if any(x in text for x in self.sad_words):
                self.total_sad_count+=1
            if any(x in text for x in self.angry_words):
                self.total_angry_count+=1
            if any(x in text for x in self.fear_words):
                self.total_fear_count+=1
            
    def print_values(self):
        values = "Happy: {}\n Sad: {}\n Angry: {}\n Scared: {}\n"
        values = values.format(self.total_happy_count,
                    self.total_sad_count,
                    self.total_angry_count,
                    self.total_fear_count)
        print(values)