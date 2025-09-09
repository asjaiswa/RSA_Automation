from selenium import webdriver
from Pages.smartphone_shop_login_page import LoginPageToShop

# ---------------------------------------------------------
# Test: Login to Smartphone Shop
# 1. Open login page
# 2. Perform successful login
# ---------------------------------------------------------
def test_smartphone_shop_login(setup: webdriver):
    driver = setup

    # Step 1: Open smartphone shop login page
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Step 2: Perform login
    login_page = LoginPageToShop(driver)
    login_page.test_successful_login()
