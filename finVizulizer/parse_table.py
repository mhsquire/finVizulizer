from bs4 import BeautifulSoup
from finVizulizer.setup_logger import logger


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
        parsed_data = []
        date = ""
        for row in html_table.findAll("tr"):

            datetime = row.td.text.split()
            if len(datetime) > 1:
                date = datetime[0]
                time = datetime[1]
            else:
                time = datetime[0]

            headline = row.a.text
            comma_headline = headline.split(',')
            if len(comma_headline) > 1:
                headline = "\\,".join(comma_headline)

            link = row.find("a").get("href")
            parsed_data.append(f'{date},{time},{headline},{link}')
        return parsed_data
