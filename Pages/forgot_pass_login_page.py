from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.read_json import load_json, get_locator
from utils.logger import get_logger  # Import your logger utility

# Initialize logger for this class/module
logger = get_logger(__name__)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Load locators and test data from forgot_password.json
        self.locators = load_json("data/forgot_password.json")
        logger.info("Loaded locators from forgot_password.json")

        # Locators for elements on the login page (loaded from JSON)
        self.forgot_password_link = get_locator(self.locators, "LoginPage", "forgot_password_link")
        self.enter_new_password_text = get_locator(self.locators, "LoginPage", "enter_new_password_text")

        # Test data for assertions
        self.assertion_text = self.locators["LoginPage"]["enter_new_password_text"]["test_data"]
        self.expected_title = self.locators["LoginPage"]["expected_title"]["test_data"]
        self.expected_text = self.locators["ForgotPage"]["enter_new_password_text"]["test_data"]

    # --------------------------
    # Action: Forgot password flow
    # --------------------------
    def go_to_forgot_password(self):
        logger.info("Starting forgot password flow")

        # Step 1: Assert the current page title is correct
        logger.info(f"Verifying page title: Expected='{self.expected_title}', Actual='{self.driver.title}'")
        assert self.driver.title == self.expected_title, (
            f"Expected title '{self.expected_title}' but got '{self.driver.title}'"
        )
        logger.info("Page title verified successfully")

        # Step 2: Click on the "Forgot password" link when clickable
        logger.info("Clicking on 'Forgot password' link")
        self.wait.until(EC.element_to_be_clickable(self.forgot_password_link)).click()
        logger.info("'Forgot password' link clicked")

        # Step 3: Wait for "Enter New Password" text to appear and fetch it
        logger.info("Waiting for 'Enter New Password' text to be visible")
        actual_text = self.wait.until(
            EC.visibility_of_element_located(self.enter_new_password_text)
        ).text
        logger.info(f"'Enter New Password' text found: '{actual_text}'")

        # Step 4: Assert the expected text matches the actual
        logger.info(f"Verifying text: Expected='{self.expected_text}', Actual='{actual_text}'")
        assert actual_text == self.expected_text, (
            f"Expected text 'Enter New Password' but got '{actual_text}'"
        )
        logger.info("Forgot password text verification passed")
