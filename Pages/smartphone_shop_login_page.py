from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from utils.read_json import load_json, get_locator
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class LoginPageToShop:
    def __init__(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10)
        # ------------------------------------------------------
        # Load locators and test data from JSON
        # ------------------------------------------------------
        self.data = load_json("data/smartphone_shop.json")
        logger.info("Loaded locators and test data from smartphone_shop.json")

        # Assign locators
        self.username = get_locator(self.data, "LoginPageToShop", "username")
        self.password = get_locator(self.data, "LoginPageToShop", "password")
        self.user = get_locator(self.data, "LoginPageToShop", "user")
        self.okay_btn = get_locator(self.data, "LoginPageToShop", "okay_btn")
        self.terms = get_locator(self.data, "LoginPageToShop", "terms")
        self.signin_btn = get_locator(self.data, "LoginPageToShop", "signin_btn")
        self.incorrect = get_locator(self.data, "LoginPageToShop", "incorrect")
        self.page_title = get_locator(self.data, "LoginPageToShop", "page_title")

    # -------------------------------------------
    # Test: Perform successful login validation
    # -------------------------------------------
    def test_successful_login(self):
        logger.info("Starting successful login test")

        # Step 1: Fill username and password
        self.driver.find_element(*self.username).send_keys(
            self.data["LoginPageToShop"]["username"]["test_data"]
        )
        self.driver.find_element(*self.password).send_keys(
            self.data["LoginPageToShop"]["password"]["test_data"]
        )
        logger.info("Entered valid username and password")

        # Step 2: Click user radio button and handle pop-up
        self.driver.find_element(*self.user).click()
        self.wait.until(EC.visibility_of_element_located(self.okay_btn)).click()
        self.wait.until(EC.invisibility_of_element(self.okay_btn))
        logger.info("User radio clicked and pop-up handled")

        # Step 3: Accept terms and click sign-in
        self.wait.until(EC.element_to_be_clickable(self.terms)).click()
        self.driver.find_element(*self.signin_btn).click()
        logger.info("Accepted terms and clicked sign-in button")

        # Step 4: Verify landing on homepage
        page_title_text = self.wait.until(
            EC.visibility_of(self.driver.find_element(*self.page_title))
        ).text
        expected_title = self.data["ProtoCommercePage"]["page_title"]["locator_value"]
        logger.info(f"Verifying homepage title: Expected='{expected_title}', Actual='{page_title_text}'")
        assert page_title_text == expected_title
        logger.info("Successful login test passed")

    # --------------------------------------------------------------------
    # Test: Perform login with incorrect credentials (expected to fail)
    # --------------------------------------------------------------------
    @pytest.mark.xfail(reason="unsuccessfully login")
    def test_unsuccessful_login(self):
        logger.info("Starting unsuccessful login test with invalid credentials")

        # Step 1: Enter incorrect username and password
        self.driver.find_element(*self.username).send_keys(
            self.data["LoginPageToShop"]["incorrect"]["test_data_username"]
        )
        self.driver.find_element(*self.password).send_keys(
            self.data["LoginPageToShop"]["incorrect"]["test_data_password"]
        )
        logger.info("Entered incorrect username and password")

        # Step 2: Click user radio and handle pop-up
        self.driver.find_element(*self.user).click()
        self.wait.until(EC.visibility_of_element_located(self.okay_btn)).click()
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.terms))).click()
        self.driver.find_element(*self.signin_btn).click()
        logger.info("Attempted login with invalid credentials")

        # Step 3: Assert error message is present
        self.wait.until(EC.presence_of_element_located(self.incorrect))
        assert "Incorrect" in self.driver.page_source
        logger.info("Unsuccessful login test verified with 'Incorrect' message")
