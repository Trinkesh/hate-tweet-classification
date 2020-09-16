import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

#api
api_key = "hdmMRWWMCXFMgA8b8hMVuFLdY"
api_secret_key = "7q8uczxDyShWeRz6S0r6zUaboP4ROlqiaxYAVNRSBX5DiTLAJf"
access_token = "1241686949091356672-W21At50Gvj0hb8oqJpZrTwCliu6nCT"
access_token_secret = "99KpTnn3jE90mnxXjmcn2GdL1nOI6wTK7lsWHRLsypVjx"

authentication = tweepy.OAuthHandler(api_key,api_secret_key)


authentication.set_access_token(access_token,access_token_secret)


api = tweepy.API(authentication,wait_on_rate_limit=True)


def get_related_tweets(text_query):
    tweets_list = []
    count = 50
    try:
        for tweet in api.search(q = text_query,count = count):
            print(tweet.text)
            
            tweets_list.append({'created_at': tweet.created_at,
                               'tweet_id': tweet.id,
                               'tweet_text':tweet.text})
        return pd.DataFrame.from_dict(tweets_list)
    except BaseException as e:
        print('failed_on_status',str(e))
        time.sleep(3)

