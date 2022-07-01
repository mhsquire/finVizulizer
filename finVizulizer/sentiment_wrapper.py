import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.downloader.download('vader_lexicon')


class SentimentWrapper:

    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()

    def score_news(self, pd_table):
        return pd_table["headline"].apply(self.vader.polarity_scores).tolist()

    # # Set column names
    # columns = ['ticker', 'date', 'time', 'headline', 'link']
    # # Convert the parsed_news list into a DataFrame called 'parsed_and_scored_news'
    # parsed_and_scored_news = pd.DataFrame(parsed_news, columns=columns)
    # # Iterate through the headlines and get the polarity scores using vader
    # scores = parsed_and_scored_news['headline'].apply(self.vader.polarity_scores).tolist()
    # # Convert the 'scores' list of dicts into a DataFrame
    # scores_df = pd.DataFrame(scores)
    # # Join the DataFrames of the news and the list of dicts
    # parsed_and_scored_news = parsed_and_scored_news.join(scores_df, rsuffix='_right')
    # # Convert the date column from string to datetime
    # parsed_and_scored_news['date'] = pd.to_datetime(parsed_and_scored_news.date).dt.dateparsed_and_scored_news.head()