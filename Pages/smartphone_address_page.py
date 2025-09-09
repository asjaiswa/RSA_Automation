from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.read_json import load_json, get_locator
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class AddressMobilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # ------------------------------------------------------
        # Load locators and test data from JSON
        # ------------------------------------------------------
        self.data = load_json("data/smartphone_shop.json")
        logger.info("Loaded locators and test data from smartphone_shop.json")

        # Assign locators using JSON
        self.countries = get_locator(self.data, "AddressMobilePage", "countries")
        self.checkbox = get_locator(self.data, "AddressMobilePage", "checkbox")
        self.submit = get_locator(self.data, "AddressMobilePage", "submit")

    # ------------------------------------------------------
    # Action: Choose country from suggestion and place order
    # ------------------------------------------------------
    def test_choose_address_and_place_order(self):
        logger.info("Starting address selection and order placement flow")

        # Step 1: Enter partial country name to trigger suggestions
        country_input = self.data["AddressMobilePage"]["countries"]["test_data"]
        logger.info(f"Typing partial country name: {country_input}")
        self.driver.find_element(*self.countries).send_keys(country_input)

        # Step 2: Wait for all matching country elements to appear
        logger.info("Waiting for country suggestions to appear")
        countries = self.wait.until(EC.presence_of_all_elements_located(self.countries))

        # Step 3: Click on "India" from suggestions
        for country in countries:
            self.wait.until(EC.visibility_of(country))
            if country.text == "India":
                logger.info("Selecting country: India")
                country.click()
                break

        # Step 4: Accept terms and conditions
        logger.info("Clicking terms and conditions checkbox")
        self.wait.until(EC.visibility_of(self.driver.find_element(*self.checkbox))).click()

        # Step 5: Submit the form to place the order
        logger.info("Clicking submit button to place order")
        self.driver.find_element(*self.submit).click()

        # Step 6: Assert that order was successful
        logger.info("Verifying success message in page source")
        assert "Success" in self.driver.page_source
        logger.info("Order placed successfully")
