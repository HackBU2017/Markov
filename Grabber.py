import twitter
import markovify

def grabber(twitter_handle):
    api = twitter.Api(consumer_key='BQRfMJOhdiARaRBwlOpo78ktp',
    consumer_secret='RxF8PngRe44jVMQDUdunfTy9KLRCqbp9NKFYX3fuHFkx2MvsHX',
    access_token_key='2498510321-AC9ycNnMzoug1iniU544RvceQkRNQxOS25qdaTr',
    access_token_secret='5odRjLJdgntK0mffliAbIARphkqDyPrJ0UjqeUMI9bmo7')

    t = api.GetUserTimeline(screen_name=twitter_handle, count = 200)

    longString = ""

    tweets = [i.AsDict() for i in t]
    #longString += [str(t['text'].encode("utf-8") for t in tweets]
    #return longString
    for t in tweets:
    #     longString += str(t['text'])
         longString += str(t['text'].encode("utf-8") for t in tweets)
         return longString
        longString += str(t['text'].encode("utf-8"))
    return longString
	screen_name='realdonaldtrump'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	alltweets = []

	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1

	while len(new_tweets) > 0:
		print ("getting tweets before %s" % (oldest))
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
		print ("...%s tweets downloaded so far" % (len(alltweets)))
	outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
	print (outtweets)
	return outtweets
