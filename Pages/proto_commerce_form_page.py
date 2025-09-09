from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.read_json import load_json, get_locator
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class PromoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # ------------------------------------
        # Load locators from JSON
        # ------------------------------------
        self.locators = load_json("data/proto_page.json")
        logger.info("Loaded locators from proto_page.json")

        self.category_link = get_locator(self.locators, "PromoPage", "category_link")
        self.name = get_locator(self.locators, "PromoPage", "name")
        self.email = get_locator(self.locators, "PromoPage", "email")
        self.password = get_locator(self.locators, "PromoPage", "password")
        self.checkbox = get_locator(self.locators, "PromoPage", "checkbox")
        self.gender_dropdown = get_locator(self.locators, "PromoPage", "gender_dropdown")
        self.employed_radio = get_locator(self.locators, "PromoPage", "employed_radio")
        self.dob = get_locator(self.locators, "PromoPage", "dob")
        self.submit = get_locator(self.locators, "PromoPage", "submit")
        self.success_alert = get_locator(self.locators, "PromoPage", "success_alert")

        # ------------------------------------
        # Load test data from JSON
        # ------------------------------------
        self.test_name = self.locators["PromoPage"]["test_data"]["username"]
        self.test_email = self.locators["PromoPage"]["test_data"]["email"]
        self.test_password = self.locators["PromoPage"]["test_data"]["password"]
        self.test_gender = self.locators["PromoPage"]["test_data"]["gender_value"]
        self.test_dob = self.locators["PromoPage"]["test_data"]["dob_value"]
        logger.info("Loaded test data for PromoPage")

    # ------------------------------------
    # Action: Fill out the promo form
    # ------------------------------------
    def fill_form(self, username=None, email=None, password=None, gender_value=None, dob_value=None):
        logger.info("Starting to fill promo form")

        # Step 1: Click category link
        logger.info("Clicking category link to open form")
        self.driver.find_element(*self.category_link).click()

        # Step 2: Fill Name, Email, Password
        logger.info(f"Entering Name: {self.test_name}")
        self.wait.until(EC.visibility_of_element_located(self.name)).send_keys(self.test_name)

        logger.info(f"Entering Email: {self.test_email}")
        self.wait.until(EC.element_to_be_clickable(self.email)).send_keys(self.test_email)

        logger.info(f"Entering Password: {self.test_password}")
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(self.test_password)

        # Step 3: Check agreement checkbox
        logger.info("Clicking agreement checkbox")
        self.wait.until(EC.element_to_be_clickable(self.checkbox)).click()

        # Step 4: Select gender from dropdown
        logger.info(f"Selecting Gender: {self.test_gender}")
        gender_element = self.wait.until(EC.visibility_of_element_located(self.gender_dropdown))
        Select(gender_element).select_by_visible_text(self.test_gender)

        # Step 5: Click Employed radio button
        logger.info("Clicking 'Employed' radio button")
        self.wait.until(EC.element_to_be_clickable(self.employed_radio)).click()

        # Step 6: Enter Date of Birth
        logger.info(f"Entering Date of Birth: {self.test_dob}")
        dob_input = self.driver.find_element(*self.dob)
        self.wait.until(EC.visibility_of(dob_input)).click()
        dob_input.send_keys(self.test_dob)

        logger.info("Promo form filled successfully")

    # ------------------------------------
    # Action: Submit the promo form
    # ------------------------------------
    def submit_form(self):
        logger.info("Submitting promo form")
        self.driver.find_element(*self.submit).click()
        logger.info("Form submitted")

    # ------------------------------------
    # Assertion: Get success alert message
    # ------------------------------------
    def get_success_message(self):
        message = self.driver.find_element(*self.success_alert).text
        logger.info(f"Success alert message: {message}")
        return message
