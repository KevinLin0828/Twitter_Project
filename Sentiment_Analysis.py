from textblob import TextBlob
import pandas as pd


#This class does sentimental anaylsis on the tweets
class Analysis:

    #This method checks whether or not polarity and subjectivity
    def polarity_and_subjectivity(self):
        read = pd.read_csv("filtered_tweets.csv") # reads in CSV file
        new_column = pd.DataFrame(read['text']) # selects the text column and puts it into a data frame
        new_column.insert(0, 'name', read['name']) # inserts column called name into the data frame
        new_column['polarity'] = new_column.apply(lambda x: TextBlob(x['text']).sentiment.polarity, axis=1) # Inserts a new column by sentimental analysis of the text column
        new_column['subjectivity'] = new_column.apply(lambda x: TextBlob(x['text']).sentiment.subjectivity, axis=1) # Inserts a new column by sentimental analysis of the text column
        new_column.to_csv('data_privacy_sentiment_analysis.csv', index=False) # puts the dataframe into a new csv file
