from selenium import webdriver
from Pages.smartphone_shop_login_page import LoginPageToShop
from Pages.smartphone_shop_page import ProtoCommercePage
from Pages.smartphone_checkout_page import CheckoutMobilePage
from Pages.smartphone_address_page import AddressMobilePage
from utils.logger import get_logger

# Initialize logger for this test module
logger = get_logger(__name__)

# ---------------------------------------------------------
# Test: Full Flow of Smartphone Shop
# Steps:
# 1. Login (handled via fixture)
# 2. Add phones to cart
# 3. Verify total amount in checkout
# 4. Choose address and place order
# ---------------------------------------------------------
def test_smartphone_shop_full_flow(login: webdriver, logger, config):
    driver = login
    logger.info("Starting test: test_smartphone_shop_full_flow")

    # Step 2: Add selected phones to the cart
    logger.info("Navigating to shop page and adding phones to cart.")
    shop_page = ProtoCommercePage(driver)
    shop_page.test_add_phone_to_cart()
    logger.info("Phones added to cart successfully.")

    # Step 3: Verify total amount on checkout page
    logger.info("Proceeding to checkout page to verify total amount.")
    checkout_page = CheckoutMobilePage(driver)
    checkout_page.test_total_amount()
    logger.info("Total amount verified successfully on checkout page.")

    # Step 4: Choose address and place the order
    logger.info("Choosing delivery address and placing the order.")
    address_page = AddressMobilePage(driver)
    order_confirmation = address_page.test_choose_address_and_place_order()  # return confirmation message
    assert "Success" in driver.page_source

    logger.info("Test passed: Smartphone Shop full flow verified successfully.")
