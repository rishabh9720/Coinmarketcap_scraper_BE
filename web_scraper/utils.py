import logging

def wait_until_present(browser, value, timeout=40):
    """
    Wait until the element identified by the specified value is present in the DOM using Splinter's API.
    """
    try:
        element = browser.find_by_css(value, wait_time=timeout)
        if element:
            return element.first
        else:
            logging.error("Element not found.")
            return None
    except Exception as e:
        logging.error(f"An error occurred while waiting for the element: {str(e)}.")
        return None

def get_text_from_element(row_element, css_selector, index=None):
    target_element = row_element.find_by_css(css_selector, wait_time=10)
    if index is not None:
        return target_element.find_by_tag("p", wait_time=10)[index].text
    return target_element.text
