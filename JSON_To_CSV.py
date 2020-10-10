import json
import csv


def organize():
    json_file = open('unfiltered_tweets_Donald_Trump.json', mode='r', encoding="utf-8").read()  # reads the JSON file
    json_data = json.loads(json_file)  # string becomes a json Python object
    csv_file = open('filtered_tweets_Donald_Trump.csv', mode='w', encoding="utf-8", newline='')  # opens csv file
    writer = csv.writer(csv_file)  # creates csv writer object
    fieldnames = ['created at', 'text', 'screen name',
                  'location', 'verified', 'followers',
                  'friends']  # fieldnames
    writer.writerow(fieldnames)  # writes fieldnames on the first row

    # gets fields from the json object and writes a row into csv file
    for tweet in json_data:
        if tweet.get('lang') != "en":  # if the tweet is not in english, don't write in csv file
            continue
        else:
            writer.writerow([tweet.get('created_at'), tweet.get('text').encode('unicode_escape'),
                            tweet.get('user').get('screen_name'), tweet.get('user').get('location'),
                            tweet.get('user').get('verified'), tweet.get('user').get('followers_count'),
                            tweet.get('user').get('friends_count')])
    csv_file.close()


if __name__ == "__main__":
    organize()
