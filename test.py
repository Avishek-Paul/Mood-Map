import json
from twitter import PyTweet
from moodmap import MoodMap

pytweet = PyTweet()
moodmap = MoodMap()

all_words = moodmap.happy_words + moodmap.sad_words + moodmap.angry_words + moodmap.fear_words

def test_get_home_timeline():
    pytweet.get_home_timeline()

def test_get_user_timeline():
    pytweet.get_user_timeline('POTUS',20)

def test_post_status():
    pytweet.post_status('Testing Testing 1 2 3')

if __name__ == '__main__':
    save_file = None#'stored_tweets.txt'
    pytweet.stream(track=all_words,
                    locations=[-74,40,-73,41], #NYC
                    saved_tweets_location=save_file)