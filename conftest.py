import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.logger import get_logger


# ---------------------------------------------------------
# Configure Pytest to use the timestamped folder
# 1. Assign report_dir to pytest config
# 2. Set HTML report path inside the same folder
# ---------------------------------------------------------
def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = os.path.join("Reports", timestamp)
    config.report_dir = report_dir
    config.option.htmlpath = os.path.join(report_dir, "report.html")


# ---------------------------------------------------------
# Logger fixture to provide logger instance to all tests
# ---------------------------------------------------------
@pytest.fixture(scope="session")
def logger(request):
    report_dir = request.config.report_dir
    return get_logger(report_dir=report_dir)


# ---------------------------------------------------------
# Pytest CLI Option to choose browser
# Usage: pytest --browser_name Chrome
# Default browser is Chrome
# ---------------------------------------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="Chrome",
        help="Browser name to open test: Chrome, Edge, Firefox"
    )


# ---------------------------------------------------------
# Pytest fixture to initialize WebDriver
# Steps:
# 1. Reads browser name from CLI option
# 2. Launches browser in private/incognito mode if supported
# 3. Maximizes window and sets implicit wait
# 4. Yields driver for test execution
# 5. Closes browser after test
# ---------------------------------------------------------
@pytest.fixture()
def setup(request):
    # Get browser name from CLI
    browser = request.config.getoption("--browser_name")

    # ----------------------
    # Browser initialization
    # ----------------------
    if browser == "Chrome":
        chrome_options = Options()
        chrome_options.add_argument("--incognito")  # Open Chrome in incognito mode
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "Edge":
        # Uncomment and configure options if needed
        # edge_options = Options()
        # edge_options.add_argument("--inprivate")
        driver = webdriver.Edge()

    elif browser == "Firefox":
        # Uncomment and configure options if needed
        # firefox_options = Options()
        # firefox_options.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox()

    else:
        raise TypeError(
            "Invalid browser name. Choose from ['Chrome', 'Edge', 'Firefox']"
        )

    # ----------------------
    # Common driver settings
    # ----------------------
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Provide driver instance to tests
    yield driver

    # Close browser after test execution
    driver.close()
