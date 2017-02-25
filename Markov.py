import tweepy
import twitter

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
client = tweepy.API(auth)

friends = client.friends()

for friend in friends:
    print friend.name
