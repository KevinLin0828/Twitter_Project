import Twitter_Stream
import time


if __name__ == "__main__":
    end_date = str(input('Input the current date in YYYY-MM-DD format\n'))
    start_date = str(input('Input the start date. The start date must be in the range of 7 days before the current date. It must be in YYYY-MM-DD format\n'))
    stream = Twitter_Stream.Streamer()
    stream.output_previous_tweets(start_date, end_date)
    time.sleep(20)
    stream.filter()
