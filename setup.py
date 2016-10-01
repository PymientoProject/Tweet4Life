import TwitterClass
import SQLClass
import DATABASE
import TWITTERDATA

"""This script search the last tweet from four different hastags on twitter, and update the SQL DB with the new tweets. It is used for update the database, because
from some reason, tweeter delete old tweets. Every time we satrt using the Tweet4Life, we have to start the setup.py"""

twitterObj = TwitterClass.TwitterClass(TWITTERDATA.CONSUMER_KEY, TWITTERDATA.CONSUMER_SECRET, TWITTERDATA.ACCESS_TOKEN, TWITTERDATA.ACCESS_TOKEN_SECRET)    #Create the twitterObj
obj = SQLClass.SQLClass(DATABASE.DB_HOST, DATABASE.DB_USER, DATABASE.DB_PASS, DATABASE.DB_NAME)     #Create the SQL object

obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarPrimera"), 1)     #Get the last tweet without hastag and add it to the database
obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarSegunda"), 2)
obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarTercera"), 3)
obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarCuarta"), 4)
