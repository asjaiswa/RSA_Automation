from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_json import get_locator, load_json
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # --------------------------
        # Load locators from JSON
        # --------------------------
        self.locators = load_json("data/green_cart.json")
        logger.info("Loaded locators from green_cart.json")

        # Element locators for the Order Page
        self.country_dropdown = get_locator(self.locators, "OrderPage", "country_dropdown")
        self.terms_checkbox = get_locator(self.locators, "OrderPage", "terms_checkbox")
        self.proceed_btn = get_locator(self.locators, "OrderPage", "proceed_btn")

    # --------------------------
    # Action: Complete the order flow
    # --------------------------
    def complete_order(self, country="India"):
        logger.info(f"Starting order completion flow for country: {country}")

        # Step 1: Select the country from dropdown
        logger.info("Waiting for country dropdown to be visible")
        dropdown = self.wait.until(EC.visibility_of_element_located(self.country_dropdown))
        Select(dropdown).select_by_visible_text(country)
        logger.info(f"Selected country: {country}")

        # Step 2: Click on the terms and conditions checkbox
        logger.info("Clicking terms and conditions checkbox")
        self.wait.until(EC.element_to_be_clickable(self.terms_checkbox)).click()

        # Step 3: Click on the proceed button to place the order
        logger.info("Clicking 'Proceed' button to place order")
        self.wait.until(EC.element_to_be_clickable(self.proceed_btn)).click()


