import logging

from coinmarketcap_scraper import settings


def wait_until_present(browser, value):
    """
    Wait until the element identified by the specified CSS selector is present in the DOM.
    ---
    Args:
        browser (Splinter.browser): The Splinter browser instance.
        value (str): CSS selector to identify the target element.
    ---
    Returns:
        Splinter.element_list.ElementList or None: The first matching element if found, else None.
    """
    try:
        element = browser.find_by_css(value, wait_time=settings.DEFAULT_WAIT_TIME)
        if element:
            return element.first
        else:
            logging.error("Element not found.")
    except Exception as e:
        logging.error(f"An error occurred while waiting for the element: {str(e)}.")

def get_text_from_element(row_element, css_selector, index=None):
    """
    Get text content from a specific element within a row element.
    ---
    Args:
        row_element (Splinter.element_list.Element): The parent element containing the target element.
        css_selector (str): CSS selector to identify the target element within the row element.
        index (int, optional): Index of the target element if multiple elements match the selector (default is None).
    ---
    Returns:
        str: Text content of the target element, or None if the element is not found.
    """
    try:
        target_element = row_element.find_by_css(css_selector, wait_time=settings.DEFAULT_WAIT_TIME)
        if index is not None:
            target_element = target_element.find_by_tag("p", wait_time=settings.DEFAULT_WAIT_TIME)[index]
        return target_element.text
    except Exception as e:
        logging.error(f"An error occurred while getting text from the element: {str(e)}.")
