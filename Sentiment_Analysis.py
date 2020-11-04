from textblob import TextBlob
import pandas as pd


#This class does sentimental anaylsis on the tweets
class Analysis:

    #This method checks whether or not polarity and subjectivity
    def polarity_and_subjectivity(self):
        read = pd.read_csv("filtered_tweets.csv") # reads in CSV file
        new_column = pd.DataFrame(read['text']) # selects the text column and puts it into a data frame
        new_column.insert(0, 'name', read['name']) # inserts column called name into the data frame
        new_column.insert(1, 'followers count',read['followers count']) # inserts column called followers count into the data frame
        new_column.insert(2, 'friends count',read['friends count']) # inserts column called followers count into the data frame
        new_column.insert(3, 'retweet count', read['retweet count'])  # inserts column called retweet count into data frame
        new_column.insert(4, 'favorite count', read['favorite count']) # inserts column called favorite count into data frame
        new_column['polarity'] = new_column.apply(lambda x: TextBlob(x['text']).sentiment.polarity, axis=1) # Inserts a new column by sentimental analysis of the text column
        new_column['subjectivity'] = new_column.apply(lambda x: TextBlob(x['text']).sentiment.subjectivity, axis=1) # Inserts a new column by sentimental analysis of the text column
        new_column.to_csv('data_privacy_sentiment_analysis.csv', index=False) # puts the dataframe into a new csv file
    
    #this method plots a scatter plot based on polarity, favorites, retweets and subjectivity.
    def scatter_plot(self):
        data = pd.read_csv("data_privacy_sentiment_analysis.csv")
        polarity = data['polarity']
        subjectivity = data['subjectivity']
        favorites = data['favorite count']
        retweet = data['retweet count']
        #The retweets count determine the size of the dots and subjectivity determines the color of the dot. Polarity and favorite count determines the X and Y field. 
        plt.scatter(polarity, favorites, s=retweet, c=subjectivity, edgecolors='black', linewidths=0.5, alpha=5)
        cbar = plt.colorbar()
        cbar.set_label('Subjectivity')
        plt.xlabel('Polarity')
        plt.ylabel('Favorite Count')
        plt.grid(True)
        plt.tight_layout()
        plt.title('sentiment analysis with favorite and retweet count')
        plt.show()
    
    #This method plots a line plot based on polarity and subjectivity.
    def line_plot(self):
        data = pd.read_csv("data_privacy_sentiment_analysis.csv")
        polarity = data['polarity']
        subjectivity = data['subjectivity']
        plt.scatter(subjectivity, polarity, edgecolors='black', linewidths=0.5)
        plt.xlabel('polarity')
        plt.ylabel('subjectivity')
        plt.title('polarity vs subjectivity')
        plt.show()
    
    #This method plots a histogram based on rhe user's polarity count and subjectivity count.
    def hist_plot(self):
        data = pd.read_csv("data_privacy_sentiment_analysis.csv")
        polarity = data['polarity']
        subjectivity = data['subjectivity']
        fig, axs = plt.subplots(1, 2, sharey=True)
        axs[0].hist(polarity, bins=10)
        axs[1].hist(subjectivity, bins=10)
        axs[0].set_title('Polarity total')
        axs[0].set_xlabel('polarity')
        axs[0].set_ylabel('number of twitter users')
        axs[1].set_title('Subjectivity total')
        axs[1].set_xlabel('subjectivity')
        plt.tight_layout()
        plt.show()
        
if __name__ == "__main__":
    analysis = Analysis()
    analysis.scatter_plot()
    analysis.line_plot()
    analysis.hist_plot()
