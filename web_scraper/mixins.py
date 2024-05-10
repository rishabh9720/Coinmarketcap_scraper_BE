from web_scraper import utils


class CryptoData:
    def __init__(self, row_element):
        self.row_element = row_element

    def is_trend_positive(self, trend_element):
        trend_indicator = trend_element.find_by_css("span > span")
        return "icon-Caret-up" in trend_indicator["class"]

    def parse_change(self, css_selector):
        change_element = self.row_element.find_by_css(css_selector)
        change_value = utils.get_text_from_element(self.row_element, css_selector)
        return f"-{change_value}" if not self.is_trend_positive(change_element) else change_value

    def fetch_coinmarket_data(self):
        return {
            "crypto_name": utils.get_text_from_element(self.row_element, "td:nth-of-type(3)", 0),
            "symbol": utils.get_text_from_element(self.row_element, "td:nth-of-type(3)", 1),
            "current_price": utils.get_text_from_element(self.row_element, "td:nth-of-type(4)"),
            "hourly_change": self.parse_change("td:nth-of-type(5)"),
            "daily_change": self.parse_change("td:nth-of-type(6)"),
            "weekly_change": self.parse_change("td:nth-of-type(7)"),
            "market_capital": utils.get_text_from_element(self.row_element, "td:nth-of-type(8)"),
            "trade_volume_usd": utils.get_text_from_element(self.row_element, "td:nth-of-type(9)", 0),
            "trade_volume_crypto": utils.get_text_from_element(self.row_element, "td:nth-of-type(9)", 1),
            "circulating_supply": utils.get_text_from_element(self.row_element, "td:nth-of-type(10)"),
        }
