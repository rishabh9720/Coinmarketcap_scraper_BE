import logging
from selenium import webdriver
from splinter import Browser

logger = logging.getLogger(__name__)

class DriverManager:
    """
    A class to manage Selenium WebDriver instances.
    ---
    Attributes:
        web_driver: The Selenium WebDriver instance.
    """

    def __init__(self):
        """
        Initializes the DriverManager with the specified URL.
        """
        self.web_driver = None

    def initialize_web_driver(self, website_url):
        """
        Initializes the Selenium WebDriver instance with optional query parameters.
        ---
        Args:
            query_params (str, optional): Query parameters to append to the URL.
        Raises:
            Exception: If an error occurs while initializing the WebDriver instance.
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        try:
            self.web_driver = Browser(driver_name='chrome', options=options,)
            self.web_driver.visit(website_url)
        except Exception as e:
            logger.error(f"Error initializing WebDriver instance: {e}")
            raise e

    def quit_web_driver(self):
        """
        Quits the Selenium WebDriver instance.
        ---
        Raises:
            Exception: If an error occurs while quitting the WebDriver instance.
        """
        try:
            if self.web_driver:
                self.web_driver.quit()
        except Exception as e:
            logger.error(f"Error quitting WebDriver instance: {e}")
            raise e
