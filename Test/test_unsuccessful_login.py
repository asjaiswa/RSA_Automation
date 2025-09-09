from selenium import webdriver
from Pages.smartphone_shop_login_page import LoginPageToShop

# ---------------------------------------------------------
# Test: Unsuccessful Login to Smartphone Shop
# 1. Open login page
# 2. Attempt login with invalid credentials
# 3. Verify error message is displayed
# ---------------------------------------------------------
def test_smartphone_shop_unsuccessful_login(setup: webdriver):
    driver = setup

    # Step 1: Open smartphone shop login page
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Step 2: Attempt login with incorrect credentials
    login_page = LoginPageToShop(driver)
    login_page.test_unsuccessful_login()
