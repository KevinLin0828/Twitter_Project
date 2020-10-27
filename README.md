# Twitter Sentiment Analysis Project #

The following project is to create a data set on Twitter. The project is to look for tweets
that are related to privacy(as in data from websites,software,etc) or trust(whether the person
accepts it or not). At the same time, detect their context. The context could be related to policy,
government, technology. Or it could be related to the number of retweets, followers, or tweets of
the person. Then, we would relate everything through sentiment analysis(whether it’s positive or
negative). The intended audience of this project is, anyone who is interested in the correlation
between trust/privacy and context of the tweets, which are related to public policies, government
and technology. The audience would be presented with graphs or data set to visualize the
correlation.


## Getting Started
First go to https://developer.twitter.com/apps to sign up. You will need the access token, access token secret, API key and API key secret.

## Installation
1. You can directly download the files by downloading as a ZIP file
2. You could also clone this GitHub repository

## Usage
When you finish downloading or cloning the respository go to Twitter_Credentials.py to input the tokens and API keys. Then run main.py, the script will ask for the dates you want to fetch from. Once the script is done running, tweets of the csv files will be generated.

## Built With
* Python 3.8
* Pandas
* Tweepy
* TextBlob
