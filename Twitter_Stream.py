import time
import csv
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
import Twitter_Credentials
from tweepy.streaming import StreamListener


# This class handles whether or not the authentication works.
class Listener(StreamListener):

    # constructor sets up the current time and the end time of the stream
    def __init__(self, time_limit=60):
        self.start_time = time.time()  # instantiates the current time
        self.end_time = time_limit  # instantiates the end time in seconds
        self.twitter_data = []  # instantiates a new list for JSON data

    def on_data(self, raw_data):
        try:
            if (time.time() - self.start_time) < self.end_time:  # calculates the amount of seconds left in the stream
                self.twitter_data.append(raw_data)   # writes JSON data into list
                return True
        except BaseException as e:
            print('failed because,', str(e))
            time.sleep(5)
            pass
        json_file = open('unfiltered_tweets_Donald_Trump.json', 'a', encoding='utf-8', newline='')  # writes into JSON file
        json_file.write(u'[\n')
        json_file.write(','.join(self.twitter_data))  # writes into JSON file with the list
        json_file.write(u'\n]')
        json_file.close()
        exit()

    # If the connection works it will return true
    def on_status(self, status):
        print(status)
        return True

    # If there is a connection problem it will return false
    def on_error(self, status_code):
        if status_code == 420:
            # Will return false if too many login attempts. Too many times authenticating with the account name.
            return False
        print(status_code)


# This class authenticates twitter's API key and access token. It also output tweets.
class Streamer:

    # The constructor authenticates the API key and access token
    def __init__(self, time_limit):
        self.listen = Listener(time_limit=time_limit)
        self.auth = OAuthHandler(Twitter_Credentials.API_KEY, Twitter_Credentials.API_KEY_SECRET)
        self.auth.set_access_token(Twitter_Credentials.ACCESS_TOKEN, Twitter_Credentials.ACCESS_TOKEN_SECRET)
        
    # This constructor authenticates the API key and access token. This constructor searches for previous tweets
    def __init__(self):
        self.auth = OAuthHandler(Twitter_Credentials.API_KEY, Twitter_Credentials.API_KEY_SECRET)
        self.auth.set_access_token(Twitter_Credentials.ACCESS_TOKEN, Twitter_Credentials.ACCESS_TOKEN_SECRET)

    # This method output any tweets that are related to the user's input
    def output_tweets(self, input_filter):
        streamer = Stream(self.auth, self.listen)
        streamer.filter(track=input_filter)
    
    # This method outputs any previous tweets up to a week from the current date. 
    def output_previous_tweets(self):
        api = API(self.auth, wait_on_rate_limit=True)
        csv_file = open('tweets_data_privacy.csv', 'w', newline='', encoding="utf-8") # opens csv file
        writer = csv.writer(csv_file)
        fieldnames = ['created at', 'text', 'name',
                      'screen name', 'location',
                      'verified', 'followers count', 'friends count',
                      'retweet count', 'favorite count']  # fieldnames
        writer.writerow(fieldnames)  # write fieldnames into header of the csv file
        # fetches for tweets based on keywords and filters out any retweets. Tweepy's API will filter out user 
        # information.
        for tweet in Cursor(api.search, q="data privacy -filter:retweets", lang="en", since="2020-10-03", until="2020-10-9").items(50000): 
            writer.writerow([tweet.created_at, tweet.text.encode('unicode_escape'),
                             tweet.user.name, tweet.user.screen_name, tweet.user.location,
                             tweet.user.verified, tweet.user.followers_count,
                             tweet.user.friends_count, tweet.retweet_count,
                             tweet.favorite_count])
            
     # this method filters out anything unrelated to data privacy.
     def filter(self):
        read = pd.read_csv("tweets_data_privacy.csv")# reads in CSV file
        df = pd.DataFrame(read)# turns CSV file into data frame
        new_data = df[~df['name'].str.contains('news|News|.com|EducationLaw|Honey|Roger Verhoeven|'
                                               'Policy Pro\'s - Business Policy Writers|Coca-Cola GB|JD Supra|'
                                               'Privacy Watch|Giridhar|QV Develop|Data Vault|Privacy Professionals Briefly|'
                                               'PrivacyPro_b|Privacy Tech Briefly|PrivacyTech_b|Hacking Essentials|Lost Coast Outpost|'
                                               'NortonRoseFulbright|Urdhva Tech|SGV Tribune|O.C. Register|Daniel Haran|Anas Najeeb|report|'
                                               'Report|SAP Customer Data Cloud')]
        #filters any names that contain any words that match with the words above.
        new_data.to_csv('filtered_tweets.csv', index=False)# returns a new CSV file

if __name__ == "__main__":
