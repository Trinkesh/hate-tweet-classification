import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

#api 
api_key = "Enter api keys"
api_secret_key = "Enter secret key"
access_token = "Enetr access token"
access_token_secret = "Enter token secret"

#use your tweeter api to get acceses to api keys

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

