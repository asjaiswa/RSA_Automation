from selenium import webdriver
from Pages.greencart_product_page import ProductPage
from Pages.greencart_checkout_page import CheckoutPage
from Pages.greencart_order_page import OrderPage
from utils.read_json import load_json
from utils.logger import get_logger

# Initialize logger for this test module
logger = get_logger(__name__)

# Load test data from JSON
data = load_json("data/green_cart.json")

# ---------------------------------------------------------
# Test: Complete Green Cart Flow
# Steps:
# 1. Search and add products to cart
# 2. Apply promo code and verify discount
# 3. Place the order
# 4. Complete the order with shipping details
# ---------------------------------------------------------
def test_green_cart_full_flow(setup: webdriver, logger, config):
    driver = setup
    logger.info("Starting test: test_green_cart_full_flow")

    # Step 1: Open Green Cart home page
    home_url = (config["URL"]["green_cart_page"])
    logger.info(f"Navigating to Green Cart home page: {home_url}")
    driver.get(home_url)

    # Step 2: Search products and add to cart
    logger.info(f"Searching for product: {data['ProductPage']['product_search']['test_data']}")
    product_page = ProductPage(driver)
    product_page.search_and_add_products(data["ProductPage"]["product_search"]["test_data"])
    logger.info("Products searched and added to cart successfully.")

    logger.info("Proceeding to checkout page.")
    product_page.go_to_checkout()

    # Step 3: Apply promo code, verify discount, and place order
    logger.info(f"Applying promo code: {data['CheckoutPage']['promo_code_input']['test_data']}")
    checkout_page = CheckoutPage(driver)
    promo_text = checkout_page.apply_promo_code(data["CheckoutPage"]["promo_code_input"]["test_data"])
    logger.info(f"Promo code applied, message received: {promo_text}")

    logger.info("Verifying discount has been applied.")
    checkout_page.verify_discount_applied()

    logger.info("Placing the order.")
    checkout_page.place_order()

    # Step 4: Complete the order by selecting country and accepting terms
    logger.info(f"Completing order with country: {data['OrderPage']['country_dropdown']['test_data']}")
    order_page = OrderPage(driver)
    order_page.complete_order(data["OrderPage"]["country_dropdown"]["test_data"])
    logger.info("Order completed successfully.")

    # Step 5: Assert that order confirmation message is present
    confirmation_msg = "Thank you, your order has been placed successfully"
    assert confirmation_msg in driver.page_source, "Order confirmation message not found in page source."
    logger.info("Order placed successfully and confirmation message verified")

    logger.info("Test passed: Green Cart full flow verified successfully.")
