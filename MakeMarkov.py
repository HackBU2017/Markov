import twitter
from Grabber import *
import markovify
import sys

def makeMarkov(twitter_handle):
    text = grabber(twitter_handle)
    print(text)
    text_model = markovify.NewlineText(text)
    print("TEST TEST TEST TEST TEST TEST TEST")
    for i in range(5):
        print(text_model.make_sentence())
    for i in range(3):
        print(text_model.make_short_sentence(140))
