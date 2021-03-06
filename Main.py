import TwitterClass
import time
import SQLClass
import DATABASE
import TWITTERDATA
import RPi.GPIO as GPIO

"""This script get the number of tweets from 4 differents hashtags, and the hastag with more tweets associated to a plant receive light. With this script we can kill a plant with tweets.
The plant with more tweets receive light, and the other, with less tweets, dies"""

pinGPIO = [21, 20, 16, 26]      #The pins of the lights

#Set the pins of the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)   #Primera
GPIO.setup(20, GPIO.OUT)   #Segunda
GPIO.setup(16, GPIO.OUT)   #Tercera
GPIO.setup(26, GPIO.OUT)   #Cuarta

numberOfTweets = [0,0,0,0]      #A array with the number of tweets of the plants

lastTweet = ["", "", "", ""]    #The last readed tweet of the plants, is for count the tweets

twitterObj = TwitterClass.TwitterClass(TWITTERDATA.CONSUMER_KEY, TWITTERDATA.CONSUMER_SECRET, TWITTERDATA.ACCESS_TOKEN, TWITTERDATA.ACCESS_TOKEN_SECRET)        #Ther twitter object of th etwitter class
obj = SQLClass.SQLClass(DATABASE.DB_HOST, DATABASE.DB_USER, DATABASE.DB_PASS, DATABASE.DB_NAME)             #Object of the SQL Custom Class

numberOfTweets[0] = obj.getNumTweetsWithNum(1)      #When you start the script the program read the number of tweets of each plant
numberOfTweets[1] = obj.getNumTweetsWithNum(2)
numberOfTweets[2] = obj.getNumTweetsWithNum(3)
numberOfTweets[3] = obj.getNumTweetsWithNum(4)

lastTweet[0] = obj.getLastTweet(1)      #When you start the script the program read the last tweet in the DB
lastTweet[1] = obj.getLastTweet(2)
lastTweet[2] = obj.getLastTweet(3)
lastTweet[3] = obj.getLastTweet(4)

while True:
    try:
        tweets = twitterObj.getTweetsWithoutRT("#SalvarPrimera")   #Receive the tweets with the hashtag
    except:
        print("Hubo un error inesperado")
        time.sleep(10)
        continue
    locatedTweet = False                                        #The Twitter API search all the tweets with the hashtag, we have to know when we need to start to count, so we create a booblean for know this

    try:
        tweets = reversed(list(tweets))
    except:
        print("Hubo un error inesperado")
        time.sleep(10)
        continue

    for tweet in tweets:                #Read the tweets, we search where are the new tweets and add the number to the DB
        tweetText = tweet.text.encode('ascii', 'xmlcharrefreplace')     #If we have a tweet in unicode, we have to pass it to ascii, with encode
        print(tweetText)

        if locatedTweet == False:           #First we have to search the tweet that is in the database as the last one, but now that tweet can or not be the last one
            if lastTweet[0] != tweetText:   #Check if the tweet in the database is the last one
                continue

                print("nada")
            else:
                print("encontrado")
                locatedTweet = True     #The program find the tweet that was in the db, now if there are new tweets the cursor will contue and add new tweets to the database
                continue

        else:       #This execute if we are reading new tweets
            lastTweet[0] = tweetText
            numberOfTweets[0] = numberOfTweets[0] + 1

            obj.insertNumTweets(obj.getNumTweetsWithNum(1) + 1, 1)      #Increas the number of tweets in the DB
            obj.setLastTweet(tweetText, 1)              #Add the new tweet to the DB
            print("sumando")

    try:
        tweets = twitterObj.getTweetsWithoutRT("#SalvarSegunda")        #The same but with other hashtag
    except:
        print("Hubo un error inesperado")
        time.sleep(10)
        continue
    locatedTweet = False

    try:
        tweets = reversed(list(tweets))
    except:
        print("Hubo un error inesperado")
        time.sleep(10)
        continue

    for tweet in tweets:  # Read the tweets, we search where are the new tweets and add the number to the DB
        tweetText = tweet.text.encode('ascii', 'xmlcharrefreplace')
        print(tweetText)

        if locatedTweet == False:
            if lastTweet[1] != tweetText:
                continue

                print("nada")
            else:
                print("encontrado")
                locatedTweet = True
                continue

        else:
            lastTweet[1] = tweetText
            numberOfTweets[1] = numberOfTweets[1] + 1

            obj.insertNumTweets(obj.getNumTweetsWithNum(2) + 1, 2)
            obj.setLastTweet(tweetText, 2)
            print("sumando")

    try:
        tweets = twitterObj.getTweetsWithoutRT("#SalvarTercera")
    except:
        print("Hubo un error inesperado")
        time.sleep(10)
        continue
    locatedTweet = False

    try:
        tweets = reversed(list(tweets))
    except:
        print("Hubo un error inesperado")
        time.sleep(10)
        continue

    for tweet in tweets:  # Read the tweets, we search where are the new tweets and add the number to the DB
        tweetText = tweet.text.encode('ascii', 'xmlcharrefreplace')
        print(tweetText)

        if locatedTweet == False:
            if lastTweet[2] != tweetText:
                continue

                print("nada")
            else:
                print("encontrado")
                locatedTweet = True
                continue

        else:
            lastTweet[2] = tweetText
            numberOfTweets[2] = numberOfTweets[2] + 1

            obj.insertNumTweets(obj.getNumTweetsWithNum(3) + 1, 3)
            obj.setLastTweet(tweetText, 3)
            print("sumando")

    try:
        tweets = twitterObj.getTweetsWithoutRT("#SalvarCuarta")
    except:
        print("Hubo un error inesperado")
        time.sleep(10)
        continue
    locatedTweet = False

    try:
        tweets = reversed(list(tweets))
    except:
        print("Hubo un error inesperado")
        time.sleep(10)
        continue

    for tweet in tweets:  # Read the tweets, we search where are the new tweets and add the number to the DB
        tweetText = tweet.text.encode('ascii', 'xmlcharrefreplace')
        print(tweetText)

        if locatedTweet == False:
            if lastTweet[3] != tweetText:
                continue

                print("nada")
            else:
                print("encontrado")
                locatedTweet = True
                continue

        else:
            lastTweet[3] = tweetText
            numberOfTweets[3] = numberOfTweets[3] + 1

            obj.insertNumTweets(obj.getNumTweetsWithNum(4) + 1, 4)
            obj.setLastTweet(tweetText, 4)
            print("sumando")


    print("-------------------------")
    print(numberOfTweets[0])
    print(numberOfTweets[1])
    print(numberOfTweets[2])
    print(numberOfTweets[3])
    print("-------------------------")

    print("el mayor es la planta" + str(numberOfTweets.index(max(numberOfTweets))))


    #When we have all the tweets, now we have to decide what we do, now we have to power on or off the lights

    for index, plant in enumerate(numberOfTweets):
        if max(numberOfTweets) == plant:
            print("ON" + str(pinGPIO[index]))
            GPIO.output(pinGPIO[index], True)
        else:
            print("OFF" + str(pinGPIO[index]))
            GPIO.output(pinGPIO[index], False)

    time.sleep(25)

