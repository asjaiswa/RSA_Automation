from selenium.webdriver.support.wait import WebDriverWait
from utils.read_json import load_json, get_locator
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class CheckoutMobilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # ------------------------------------------------------
        # Load locators and test data from JSON
        # ------------------------------------------------------
        self.locators = load_json("data/checkout_mobile.json")
        logger.info("Loaded locators and test data from checkout_mobile.json")

        # Assign element locators
        self.total_tr = get_locator(self.locators, "CheckoutMobilePage", "total_tr")
        self.bill_price_locator = get_locator(self.locators, "CheckoutMobilePage", "bill_price")
        self.place_order_button = get_locator(self.locators, "CheckoutMobilePage", "place_order_button")
        self.expected_bill_price = self.locators["CheckoutMobilePage"]["bill_price"]["test_data"]

    # ------------------------------------------------------
    # Action: Verify total amount and place order
    # ------------------------------------------------------
    def test_total_amount(self):
        logger.info("Starting total amount verification and order placement")

        # Step 1: Find all product/summary rows
        total_rows = self.driver.find_elements(*self.total_tr)
        logger.info(f"Found {len(total_rows)} product/summary rows in checkout")

        # Step 2: Get bill total value (remove currency symbol)
        bill_price = self.driver.find_element(*self.bill_price_locator).text[3:]
        logger.info(f"Bill price found on UI: {bill_price}, Expected: {self.expected_bill_price}")

        # Step 3: Click on place order button
        logger.info("Clicking on place order button")
        self.driver.find_element(*self.place_order_button).click()

        # Step 4: Validate that the total matches the expected value
        assert bill_price == self.expected_bill_price, (
            f"Expected bill to be {self.expected_bill_price} but got {bill_price}"
        )
        logger.info("Total amount verified and order placed successfully")
