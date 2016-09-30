import TwitterClass
import time
import SQLClass
import DATABASE
import RPi.GPIO as GPIO
consumer_key = ""               #GO TO TWITTER TO FIND THIS INFO
consumer_secret = ""
access_token = ""
access_token_secret = ""


pinGPIO = [21, 20, 16, 26]

#Set the pins of the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)   #Primera
GPIO.setup(20, GPIO.OUT)   #Segunda
GPIO.setup(16, GPIO.OUT)   #Tercera
GPIO.setup(26, GPIO.OUT)   #Cuarta

numberOfTweets = [0,0,0,0]      #A array with the number of tweets of the plants

lastTweet = ["", "", "", ""]    #The last readed tweet of the plants, is for count the tweets

twitterObj = TwitterClass.TwitterClass(consumer_key, consumer_secret, access_token, access_token_secret)        #Ther twitter object of th etwitter class
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
    tweets = twitterObj.getTweetsWithoutRT("#SalvarPrimera")   #Receive the tweets with the hashtag
    locatedTweet = False                                        #The Twitter API search all the tweets with the hashtag, we have to know when we need to start to count, so we create a booblean for know this

    for tweet in reversed(list(tweets)):                #Read the tweets, we search where are the new tweets and add the number to the DB

        tweetText = tweet.text.encode('ascii', 'xmlcharrefreplace')
        print(tweetText)

        if locatedTweet == False:
            if lastTweet[0] != tweetText:
                continue

                print("nada")
            else:
                print("encontrado")
                locatedTweet = True
                continue

        else:
            lastTweet[0] = tweetText
            numberOfTweets[0] = numberOfTweets[0] + 1

            obj.insertNumTweets(obj.getNumTweetsWithNum(1) + 1, 1)
            obj.setLastTweet(tweetText, 1)
            print("sumando")

    tweets = twitterObj.getTweetsWithoutRT("#SalvarSegunda")        #The same but with other hashtag
    locatedTweet = False

    for tweet in reversed(list(tweets)):
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

    tweets = twitterObj.getTweetsWithoutRT("#SalvarTercera")
    locatedTweet = False

    for tweet in reversed(list(tweets)):
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

    tweets = twitterObj.getTweetsWithoutRT("#SalvarCuarta")
    locatedTweet = False

    for tweet in reversed(list(tweets)):
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

