import twitter
from Grabber import *
import markovify

def makeMarkov(twitter_handle):
    text = grabber(twitter_handle)
    print(text)
    text_model = markovify.Text(text)
    for i in range(5):
        print(text_model.make_sentence())
    for i in range(3):
        print(text_model.make_short_sentence(140))
