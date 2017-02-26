import twitter
from Grabber import *
import markovify
import sys

def makeMarkov(twitter_handle):
    print(text)
    text_model = markovify.NewlineText(text)
    for i in range(5):
        print(text_model.make_sentence())
    for i in range(3):
        print(text_model.make_short_sentence(140))
