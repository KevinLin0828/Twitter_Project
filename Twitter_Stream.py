import time
from tweepy import OAuthHandler
from tweepy import Stream
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

    # This method output any tweets that are related to the user's input
    def output_tweets(self, input_filter):
        streamer = Stream(self.auth, self.listen)
        streamer.filter(track=input_filter)

    # sort.convert_to_csv()


if __name__ == "__main__":
    filter_list = ["Donald Trump"]
    stream = Streamer(time_limit=5000)
    stream.output_tweets(filter_list)