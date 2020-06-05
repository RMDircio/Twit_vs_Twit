# twit_app/services/twitter_service.py

import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print('Auth', type(auth))

api = tweepy.API(auth)
print('API Client', type(api))

if __name__ == "__main__":

    user = api.get_user('s2ts')
    print(type(user))

    # print info about user
    # too see all usable methods: dir(user)
    # pretty print the list: 
    # >>> from pprint import pprint
    # >>> pprint(user._json)
    # see all useable methods on api: pprint(dir(api))
    # see all useable methods on tweets:
    # >>> tweets =api.user_timeline('s2t2')
    # >>> pprint(dir(tweets))
    # see the full text of tweet
    # >>> tweets = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    # >>> tweets[0].full_text

    print(user.id)
    print(user.screen_name)
    print(user.followers_count)

    tweets = api.user_timeline('s2t2', tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)

    # for loop tweets
    for tweet in tweets:
        print('-------')
        print(tweet.id, tweet.full_text)
