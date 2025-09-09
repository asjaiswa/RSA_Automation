from selenium import webdriver
from Pages.smartphone_shop_login_page import LoginPageToShop
from Pages.smartphone_shop_page import ProtoCommercePage
from Pages.smartphone_checkout_page import CheckoutMobilePage
from Pages.smartphone_address_page import AddressMobilePage

# ---------------------------------------------------------
# Test: Full Flow of Smartphone Shop
# 1. Login
# 2. Add phones to cart
# 3. Verify total amount in checkout
# 4. Choose address and place order
# ---------------------------------------------------------
def test_smartphone_shop_full_flow(setup: webdriver):
    driver = setup

    # Step 1: Open smartphone shop login page
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Step 2: Login to the shop
    login_page = LoginPageToShop(driver)
    login_page.test_successful_login()

    # Step 3: Add selected phones to the cart
    shop_page = ProtoCommercePage(driver)
    shop_page.test_add_phone_to_cart()

    # Step 4: Verify total amount in checkout page
    checkout_page = CheckoutMobilePage(driver)
    checkout_page.test_total_amount()

    # Step 5: Choose address and place the order
    address_page = AddressMobilePage(driver)
    address_page.test_choose_address_and_place_order()
