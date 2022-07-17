from bs4 import BeautifulSoup
from setup_logger import logger


class ParseTable:

    @classmethod
    def read_html(cls, response):
        parsed_response = BeautifulSoup(response, "html.parser")
        return parsed_response

    @classmethod
    def find_news(cls, parsed_response: BeautifulSoup):
        table = parsed_response.find(id="news-table")
        if not table:
            logger.error("Can't find news of ticker.")
            return None
        return table

    @classmethod
    def parse_news(cls, html_table: BeautifulSoup):
        date = ""
        news_list = []
        for row in html_table.findAll("tr"):
            datetime = row.td.text.split()
            if len(datetime) > 1:
                date = datetime[0]
                time = datetime[1]
            else:
                time = datetime[0]

            headline = row.a.text
            link = row.find("a").get("href")

            news_list.append([date, time, headline, link])
        return news_list