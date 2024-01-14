import re
import csv
import pprint
import pathlib
import logging
import json
import requests
from bs4 import BeautifulSoup
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from helper import BASE_URLS, PAGE_ELEMENT_PATHS, get_element_for_path

# import scraper.helper

script_path = pathlib.Path(__file__).parent.resolve()

logging.basicConfig(filename="logs.log", level=logging.INFO)
# truncating log file before new run
with open("logs.log", "w"):
    pass

class Scraper:
    """
    Encapsulates all the logic for the web scraper.
    """

    def __init__(self) -> None:
        # self.base_url = "https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version"
        return
        
    def scrape(self, page_list_page: str) -> list:
        """
            Get all of the wikipedia articles from that page
        """
        wikipedia_data_headers = ["article_key", "article_name", "article_url"]
        wikipedia_data = []
        # initialize data headers

        try:
            wiki_page_resp = requests.get(page_list_page)
            wiki_page_soup = BeautifulSoup(wiki_page_resp.text, "html.parser")
        except requests.exceptions.RequestException as e:
            logging.log(e)

        # next_page_
        next_page_a_tag = get_element_for_path(wiki_page_soup, PAGE_ELEMENT_PATHS["WIKIPEDIA_PAGE_LIST_PAGE"]["NEXT_PAGE_OF_LISTED_ARTICLES"])
        next_page_url_path = next_page_a_tag.get("href")

        page_list_list_items = get_element_for_path(wiki_page_soup, PAGE_ELEMENT_PATHS["WIKIPEDIA_PAGE_LIST_PAGE"]["ALL_PAGE_LIST_ITEMS"])
        # page_list_a_tags = page_list_page_links.
        # summary_text_links = get_element_for_path(wiki_page_soup, PAGE_ELEMENT_PATHS["WIKIPEDIA_ARTICLE_PAGE"]["SUMMARY_TEXT_LINKS"])

        page_list_a_tags = list(map(lambda li: li.find('a'), page_list_list_items))

        wikipedia_article_key_regex = r'/wiki/(.*)'        

        for a_tag in page_list_a_tags:
            article_name = a_tag.get('title')
            href_value = a_tag.get('href')
            article_key_match = re.search(wikipedia_article_key_regex, href_value)

            if article_key_match:
                article_key = article_key_match.group(1)
            else:
                raise Exception(f"Unexpected href value ({href_value}) on article ({article_name})")

            data_row = (article_key, article_name)
            row_data = {}
            for i, dt in enumerate(data_row):
                row_data[wikipedia_data_headers[i]] = dt
            wikipedia_data.append(row_data)
            
            print(f"a tag: {a_tag}")
        
        return (wikipedia_data, next_page_url_path)

        

    def convert_to_csv(self, scraped_data: list, file_name: str, data_level: str) -> None:
        """
        Converts a list of dictionaries to a csv file

        Args:
            scraped_data (list[dict]): List of dictionaries containing each page's data
            page_list_page (str): String specifiying the unique url key of the wikipedia page
            data_level (str): Signifies the level of data, ie, gold, bronze, silver
        """


        with open(f"../csv/{file_name}-{data_level}.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=scraped_data[0].keys())
            writer.writeheader()
            writer.writerows(scraped_data)


if __name__ == "__main__":
    scraper = Scraper()
    # starting_point_path = "Special:AllPages/"
    starting_point_path = "/w/index.php?title=Special:AllPages&from=%21"
    pageNumber = 0
    # https://en.wikipedia.org/w/index.php?title=Special:AllPages&from=%21
    # https://en.wikipedia.org/w/index.php?title=Special:AllPages&from=%22Alecu+Russo%22+State+University+of+B%C4%83l%C8%9Bi
    next_wikipedia_page_list = f"https://en.wikipedia.org{starting_point_path}"
    (new_pages, next_starting_point_path) = scraper.scrape(page_list_page=next_wikipedia_page_list)

    timestamp_milliseconds = int(time.time() * 1000)
    csv_file_name = f"page_{pageNumber}_time_{timestamp_milliseconds}"

    print(f"new pages: {new_pages}")
    scraper.convert_to_csv(scraped_data=new_pages, file_name=csv_file_name, data_level="bronze")
