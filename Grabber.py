import twitter
import markovify

def grabber(twitter_handle):
    api = twitter.Api(consumer_key='BQRfMJOhdiARaRBwlOpo78ktp',
      consumer_secret='RxF8PngRe44jVMQDUdunfTy9KLRCqbp9NKFYX3fuHFkx2MvsHX',
      access_token_key='2498510321-AC9ycNnMzoug1iniU544RvceQkRNQxOS25qdaTr',
      access_token_secret='5odRjLJdgntK0mffliAbIARphkqDyPrJ0UjqeUMI9bmo7')

    {"id": 16133, "location": "Philadelphia", "name": "bear"}

    t = api.GetUserTimeline(screen_name=twitter_handle)

    longString = ""

    tweets = [i.AsDict() for i in t]
    for t in tweets:
        longString += str(t['text'])
    return longString
