import tweepy

class TwitterClass:
    '''Twitter class for use with twitter'''
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consummer_key = consumer_key
        self.consummer_secret = consumer_secret
        self.access_token = access_token
        self.access_toke_secret = access_token_secret

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def getTweets(self, url):
        public_tweets = self.api.search([])
        for tweet in public_tweets:
            print(tweet.text)

    def searchTweets(self, hashtag, limit):
        cursor = tweepy.Cursor(self.api.search,
                               q=hashtag,
                               count=100,
                               result_type="recent").items(limit)

        for tweet in cursor:
            print(tweet.text)

    def searchTweetsWithoutRT(self, hashtag, limit):
        cursor = tweepy.Cursor(self.api.search,
                               q=hashtag + " -RT",
                               count=100,
                               result_type="recent").items(limit)

        for tweet in cursor:
            print(tweet.text)

    def getLastTweetWithoutRT(self, hashtag):
        cursor = tweepy.Cursor(self.api.search,
                               q=hashtag + " -RT",
                               count=100,
                               result_type="recent").items(1)

        return cursor.next().text

    def getTweetsWithoutRT(self, hashtag):
        cursor = tweepy.Cursor(self.api.search,
                               q=hashtag + " -RT",
                               count=100,
                               result_type="recent").items(100)

        return cursor

