from parse_table import ParseTable
from sentiment_wrapper import SentimentWrapper
from request_wrapper import RequestWrapper
import pandas as pd


if __name__ == "__main__":
    request = RequestWrapper()
    response = request.get("https://finviz.com/quote.ashx?t=" + "TSLA")

    bs_response = ParseTable.read_html(response.text)
    bs_news = ParseTable.find_news(bs_response)
    parsed_news = ParseTable.parse_news(bs_news)

    columns = ["date", "time", "headline", "link"]
    pd_news = pd.DataFrame(parsed_news, columns=columns)

    sw = SentimentWrapper()
    pd_table = sw.score_news(pd_news)
    pd_table_df = pd.DataFrame(pd_table)
    data = pd_news.join(pd_table_df, rsuffix="_right")

    data["date"] = pd.to_datetime(data.date).dt.date
    print(data)