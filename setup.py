import TwitterClass
import SQLClass
import DATABASE

consumer_key = "RqMxLrOKUXRCQ2v1hkjjcrz0E"               #GO TO TWITTER TO FIND THIS INFO
consumer_secret = "pK3KxtqYZz82sVrpa2NFXQlRXN5vTkh82SZEgwZItVkbiy1iS6"
access_token = "757628469484331008-uVRkfHjzXTzly34eKHvNWmZTYI7CVKA"
access_token_secret = "vGpwcFqeBEBpL1fvsgKhYDMqc1ebDXL2X9tsFpSGKqgV8"

numberOfTweets = [0,0,0,0]

lastTweet = ["", "", "", ""]

twitterObj = TwitterClass.TwitterClass(consumer_key, consumer_secret, access_token, access_token_secret)
obj = SQLClass.SQLClass(DATABASE.DB_HOST, DATABASE.DB_USER, DATABASE.DB_PASS, DATABASE.DB_NAME)

obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarPrimera"), 1)
obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarSegunda"), 2)
obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarTercera"), 3)
obj.setLastTweet(twitterObj.getLastTweetWithoutRT("#SalvarCuarta"), 4)