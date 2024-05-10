import logging

from web_scraper.mixins import CryptoData
from web_scraper import utils

logger = logging.getLogger(__name__)

class CoinMarketCapScraper:
    def __init__(self, browser):
        self.browser = browser

    def fetch_chunk_data(self, chunk_count):
        results = []
        try:
            utils.wait_until_present(
                self.browser,
                '.cmc-table tbody tr:nth-of-type({})'.format(
                    (chunk_count+1) * 5 # check the value
                )
            )
            table_element = self.browser.find_by_css('.cmc-table', wait_time=10)
            body_element = table_element.find_by_tag('tbody', wait_time=10)
            data_rows = body_element.find_by_tag('tr', wait_time=10)

            chunk_size = 5
            start_index = chunk_count * chunk_size
            end_index = (chunk_count + 1) * chunk_size
            parsed = data_rows[start_index:end_index]

            for i, data_row in enumerate(parsed):
                parser = CryptoData(data_row)
                info = parser.fetch_coinmarket_data()
                results.append(info)
        except Exception as e:
            # Handle the exception here, such as logging or printing an error message
            logger.error(f"An error occurred while fetching table data: {e}")
        return results

    def fetch_table_data(self, page_count=3):
        results = []
        if self.browser:
            total_chunks = 20
            for page_num in range(1, page_count + 1):
                scroll_step = 500
                page_height = 0
                chunk_count = 0
                while chunk_count < total_chunks:
                    results.extend(self.fetch_chunk_data(chunk_count))
                    updated_height = page_height + scroll_step
                    self.browser.execute_script(
                        f'window.scrollTo({page_height}, {updated_height});'
                    )
                    page_height = updated_height
                    chunk_count += 1
                self.browser.visit(f'https://coinmarketcap.com/?page={page_num}')

                if page_num >= page_count:
                    break
        return results
