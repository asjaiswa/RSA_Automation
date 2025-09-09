import json
from selenium.webdriver.common.by import By


# ----------------------------------------
# Load JSON data from the given file path
# ----------------------------------------
def load_json(file_path):
    """
    Load a JSON file and return its content as a Python dictionary.

    Args:
        file_path (str): Relative or absolute path to the JSON file.

    Returns:
        dict: Parsed JSON data.
    """
    with open(file_path, 'r') as f:
        return json.load(f)


# ------------------------------------------------------------------
# Extract locator tuple (By.<TYPE>, "value") from a JSON structure
# ------------------------------------------------------------------
def get_locator(locators, page_name, locator_name):
    """
    Fetch the locator tuple (By.<TYPE>, value) for the given page and element.

    Args:
        locators (dict): JSON data loaded using load_json().
        page_name (str): Name of the page section in the JSON.
        locator_name (str): Name of the locator inside the page section.

    Returns:
        tuple: (By.<LOCATOR_TYPE>, "locator_value")
    """
    locator = locators[page_name][locator_name]
    by = getattr(By, locator["locator_type"].upper())
    return by, locator["locator_value"]
