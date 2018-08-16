import json
from twitter import PyTweet
from streamhandler import StreamHandler
from conf.settings import all_words

pytweet = PyTweet()

search_words = list()
for list_ in all_words:
    search_words += all_words[list_]

def test_get_home_timeline():
    pytweet.get_home_timeline()

def test_get_user_timeline():
    pytweet.get_user_timeline('POTUS',20)

def test_post_status():
    pytweet.post_status('Testing Testing 1 2 3')

if __name__ == '__main__':
    try:
        pytweet.stream(track=search_words,
                        #locations=[-74,40,-73,41], #NYC
                        )
    except KeyboardInterrupt:
        print("External Interrupt Detected. Exiting program...")
    except Exception as e:
        print("Exception occurred. Trying again...")
        pytweet.stream(track=search_words,
                #locations=[-74,40,-73,41], #NYC
                )

