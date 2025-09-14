from selenium import webdriver
from Pages.proto_commerce_form_page import PromoPage
from utils.logger import get_logger

# ---------------------------------------------------------
# Test: Verify Promo Page Form Submission
# Steps:
# 1. Login to the smartphone shop
# 2. Fill promo form with user details
# 3. Submit the form
# 4. Verify success message
# ---------------------------------------------------------
def test_promo(login: webdriver, logger, config):
    driver = login
    logger.info("Starting test: test_promo")

    # Step 1 & 2: Assume login already handled in fixture, move to promo form
    logger.info("Navigating to Promo Page...")
    promo_page = PromoPage(driver)

    # Step 3: Fill the promo form with test data
    logger.info("Filling promo form with username, email, password, gender, and DOB.")
    promo_page.fill_form(
        username=promo_page.name,
        email=promo_page.email,
        password=promo_page.password,
        gender_value=promo_page.test_gender,
        dob_value=promo_page.dob
    )
    logger.info("Promo form filled successfully.")

    # Step 4: Submit the form
    logger.info("Submitting the promo form.")
    promo_page.submit_form()
    logger.info("Promo form submitted successfully.")

    # Step 5: Verify success message after form submission
    success_message = promo_page.get_success_message()
    logger.info(f"Captured success message: {success_message}")
    assert "Success" in success_message, "Promo form submission failed!"
    logger.info("Test passed: Promo form submission verified successfully.")
