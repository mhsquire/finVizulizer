import json

import pytest
from bs4 import BeautifulSoup
import nltk

from finVizulizer.sentiment_wrapper import SentimentWrapper

nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

@pytest.fixture
def init_sentiment_wrapper():
    return SentimentWrapper()

@pytest.fixture
def parsed_json_table():
    with open("tests/helpers/parsenews.json") as file:
        json_table = json.loads(file.read())
    return json_table

class TestSentimentWrapper:

    def test_init(self):
        assert True

    def test_score_news(self, init_sentiment_wrapper, parsed_json_table):
        columns = ["date", "time", "headline", "link"]
        panda_table = pd.DataFrame(parsed_json_table, columns=columns)
        sentiment_wrapper = init_sentiment_wrapper
        scores = sentiment_wrapper.score_news(panda_table)
        with open("tests/helpers/sentiment_scores.json", 'r') as file:
            example_scores = json.loads(file.read())
        assert scores == example_scores

