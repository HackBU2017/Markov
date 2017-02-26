import twitter
import markovify

def grabber():
    api = twitter.Api(consumer_key='BQRfMJOhdiARaRBwlOpo78ktp',
      consumer_secret='RxF8PngRe44jVMQDUdunfTy9KLRCqbp9NKFYX3fuHFkx2MvsHX',
      access_token_key='2498510321-AC9ycNnMzoug1iniU544RvceQkRNQxOS25qdaTr',
      access_token_secret='5odRjLJdgntK0mffliAbIARphkqDyPrJ0UjqeUMI9bmo7')


    {"id": 16133, "location": "Philadelphia", "name": "bear"}

    t = api.GetUserTimeline(screen_name='incrubberduck')

    longString = ""

    tweets = [i.AsDict() for i in t]
    for t in tweets:
        longString += str(t['text']) + "\n"
    return longString

def makeMarkov():
    text = grabber()
    print(text)
    text_model = markovify.NewlineText(text)
    for i in range(5):
        print(text_model.make_sentence())
    for i in range(3):
        print(text_model.make_short_sentence(140))

makeMarkov()
