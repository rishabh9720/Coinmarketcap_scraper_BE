import logging

from django.conf import settings
from coinmarketcap_scraper.celery import app
from web_scraper import scraper
from web_scraper import driver

logger = logging.getLogger(__name__)

@app.task
def scrape_coinmarket_data_and_post():
    """
    Celery task to scrape CoinMarketCap data and perform post-processing tasks.
    This task initializes a web driver, scrapes data using CoinMarketCapScraper, and processes the data.
    """
    # Initialize the web driver
    web_driver_obj = driver.DriverManager()

    # Initialize the CoinMarketCapScraper
    web_scraper_obj = scraper.CoinMarketCapScraper(web_driver_obj.web_driver)

    # Fetch data from CoinMarketCap table
    crypto_scrapped_data = web_scraper_obj.fetch_table_data()
    web_driver_obj.quit_web_driver()
    print('crypto_scrapped_data', crypto_scrapped_data)
