from selenium import webdriver
from Pages.greencart_product_page import ProductPage
from Pages.greencart_checkout_page import CheckoutPage
from Pages.greencart_order_page import OrderPage
from utils.read_json import load_json

# Load test data from JSON
data = load_json("data/green_cart.json")

# ---------------------------------------------------------
# Test: Complete Green Cart Flow
# 1. Search and add products to cart
# 2. Apply promo code and verify discount
# 3. Place the order
# 4. Complete the order with shipping details
# ---------------------------------------------------------
def test_green_cart_full_flow(setup: webdriver):
    driver = setup

    # Step 1: Open Green Cart home page
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    # Step 2: Search products and add to cart
    product_page = ProductPage(driver)
    product_page.search_and_add_products(data["ProductPage"]["product_search"]["test_data"])
    product_page.go_to_checkout()

    # Step 3: Apply promo code, verify discount, and place order
    checkout_page = CheckoutPage(driver)
    promo_text = checkout_page.apply_promo_code(data["CheckoutPage"]["promo_code_input"]["test_data"])
    checkout_page.verify_discount_applied()
    checkout_page.place_order()

    # Step 4: Complete the order by selecting country and accepting terms
    order_page = OrderPage(driver)
    order_page.complete_order(data["OrderPage"]["country_dropdown"]["test_data"])
