from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.read_json import get_locator, load_json
from utils.logger import get_logger  # Import the logger utility

# Initialize logger for this class/module
logger = get_logger(__name__)

class ForgotPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # --------------------------
        # Load locators from JSON
        # --------------------------
        self.locators = load_json("data/forgot_password.json")
        logger.info("Loaded locators from forgot_password.json")

        # Element locators (loaded from JSON)
        self.enter_new_password_text = get_locator(self.locators, "ForgotPage", "enter_new_password_text")
        self.email_input = get_locator(self.locators, "ForgotPage", "email_input")
        self.password_input = get_locator(self.locators, "ForgotPage", "password_input")
        self.confirm_password_input = get_locator(self.locators, "ForgotPage", "confirm_password_input")
        self.submit_button = get_locator(self.locators, "ForgotPage", "submit_button")

        # --------------------------
        # Test data from JSON
        # --------------------------
        self.expected_text = self.locators["ForgotPage"]["enter_new_password_text"]["test_data"]
        self.email = self.locators["ForgotPage"]["email_input"]["test_data"]
        self.password = self.locators["ForgotPage"]["password_input"]
        self.expected_page_title = self.locators["ForgotPage"]["expected_page_title"]["test_data"]

    # --------------------------
    # Action: Reset password flow
    # --------------------------
    def reset_password(self, email="demo@gmail.com", new_password="Pass@1212"):
        logger.info("Starting reset password flow")

        # Step 1: Assert presence of "Enter New Password" heading
        logger.info("Verifying 'Enter New Password' text is displayed")
        actual_text = self.wait.until(
            EC.visibility_of_element_located(self.enter_new_password_text)
        ).text
        logger.info(f"Found text: '{actual_text}' | Expected: '{self.expected_text}'")
        assert actual_text == self.expected_text, (
            f"Expected 'Enter New Password' but got '{actual_text}'"
        )
        logger.info("'Enter New Password' text verification passed")

        # Step 2: Fill in the reset password form
        logger.info(f"Entering email: {email}")
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)

        logger.info(f"Entering new password")
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(new_password)
        self.wait.until(EC.visibility_of_element_located(self.confirm_password_input)).send_keys(new_password)
        logger.info("Filled all password fields")

        # Step 3: Click the submit button
        logger.info("Clicking the submit button")
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()

        # Step 4: Assert that page navigated successfully based on the expected title
        logger.info(f"Verifying page title after submission: Expected='{self.expected_page_title}'")
        assert self.wait.until(EC.title_is(self.expected_page_title)), (
            f"Expected page title to be '{self.expected_page_title}' after submission"
        )
        logger.info("Reset password flow completed successfully")
