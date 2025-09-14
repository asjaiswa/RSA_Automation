from selenium import webdriver
from Pages.practice_page import PracticePage
from utils.logger import get_logger

# Initialize logger for this test module
logger = get_logger(__name__)

# ---------------------------------------------------------
# Test: Complete Practice Page Automation
# Steps:
# 1. Open the Practice Page
# 2. Fill form with radio buttons, dropdowns, and checkboxes
# 3. Handle alerts, windows, tabs, iframes
# 4. Perform table validations
# ---------------------------------------------------------
def test_practice_page(setup: webdriver, logger, config):
    driver = setup
    logger.info("Starting test: test_practice_page")

    # Step 1: Open the Practice Page URL
    practice_url = (config["URL"]["practice_page"])
    logger.info(f"Navigating to Practice Page: {practice_url}")
    driver.get(practice_url)

    # Step 2: Perform all actions on Practice Page
    logger.info("Initializing PracticePage object and performing actions.")
    practice_page = PracticePage(driver)
    practice_page.fill_the_form()
    logger.info("Form interactions, alerts, windows, tabs, iframes, and table validations completed successfully.")

    logger.info("Test passed: Practice Page automation verified successfully.")
