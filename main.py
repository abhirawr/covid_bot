import tweepy
import requests
from datetime import datetime

#TWITTER API INITIALIZATION
consumer_key = 'DH2mxQWuKlKjvTQ34GXVRJ2iE' 
consumer_secret = 'FeOCVyyjjbqtkhX3v3xMI3WaMMLL4bOttUmuvwqLKNpIXwWJdm'
access_token = '1302277618801217539-HI2IwnhUTWcug4n729aSgNmeFZpzUY' 
access_token_secret = 'nEXQRtRH9KrzPjcctvoxMVOyxkQDysKzj6M7B45RbclTe'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#ACCESSING OPEN COVID19 API
covidDailyURL = 'https://api.covid19api.com/world/total'
covidDaily = requests.get(covidDailyURL).json()

#FORMATTING DATA FOR DAILY TWEET
Cases = covidDaily['TotalConfirmed']
Deaths = covidDaily['TotalDeaths']
Recovered = covidDaily['TotalRecovered']

desc = "TODAYS STATS [" + str(datetime.today().date()) + "]\nConfirmed Cases: " + str(Cases) + "\nConfirmed Deaths: "  + str(Deaths) + "\nConfirmed Recovered: " + str(Recovered) + "\nThat's alot! Stay safe and dont forget to wear a mask!"

print(desc)

