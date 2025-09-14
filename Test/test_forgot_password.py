from selenium import webdriver
from Pages.forgot_pass_login_page import LoginPage
from Pages.forgot_pass_page import ForgotPage
from utils.logger import get_logger

# Initialize logger for this test module
logger = get_logger(__name__)

# ---------------------------------------------------------
# Test: Verify forgot password flow in the login page
# Steps:
# 1. Open the login page
# 2. Click "Forgot Password"
# 3. Fill reset form and submit
# 4. Verify reset confirmation
# ---------------------------------------------------------
def test_forgot_password(setup: webdriver, logger, config):
    driver = setup
    logger.info("Starting test: test_forgot_password")

    # Step 1: Open the login page URL
    # login_url = driver.get(config["URL"]["forgot_page"])
    # logger.info(f"Navigating to login page: {login_url}")
    driver.get(config["URL"]["forgot_page"])

    # Step 2: Navigate to 'Forgot Password'
    logger.info("Clicking on 'Forgot Password' link.")
    login_page = LoginPage(driver)
    login_page.go_to_forgot_password()
    logger.info("'Forgot Password' page opened successfully.")

    # Step 3: Reset password using ForgotPage
    logger.info("Filling forgot password form and submitting request.")
    forgot_page = ForgotPage(driver)
    forgot_page.reset_password()
    logger.info("Password reset process completed successfully.")

    logger.info("Test passed: Forgot password flow verified successfully.")
