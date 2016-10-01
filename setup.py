import TwitterClass
import SQLClass
import DATABASE
import TWITTERDATA

numberOfTweets = [0,0,0,0]

lastTweet = ["", "", "", ""]

twitterObj = TwitterClass.TwitterClass(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
obj = SQLClass.SQLClass(DATABASE.DB_HOST, DATABASE.DB_USER, DATABASE.DB_PASS, DATABASE.DB_NAME)

obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarPrimera"), 1)
obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarSegunda"), 2)
obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarTercera"), 3)
obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarCuarta"), 4)
