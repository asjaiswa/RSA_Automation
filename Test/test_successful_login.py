from selenium import webdriver
from Pages.smartphone_shop_login_page import LoginPageToShop

# ---------------------------------------------------------
# Test: Login to Smartphone Shop
# 1. Open login page
# 2. Perform successful login
# ---------------------------------------------------------
def test_smartphone_shop_successful_login(login: webdriver, logger, config):
    driver = login

    # Step 3: Verify login success
    assert "Shop" in driver.title or driver.current_url != config["URL"]["login_page"], \
        "Login failed - user not redirected after successful login"
    logger.info("Successfully logged in to Smartphone Shop")


# ---------------------------------------------------------
# Test: Unsuccessful Login to Smartphone Shop
# 1. Open login page
# 2. Attempt login with invalid credentials
# 3. Verify error message is displayed
# ---------------------------------------------------------
def test_smartphone_shop_unsuccessful_login(setup: webdriver, logger, config):
    driver = setup
    driver.get(config["URL"]["login_page"])

    # Step 2: Attempt login with incorrect credentials
    login_page = LoginPageToShop(driver)
    login_page.test_unsuccessful_login()

    # Step 3: Verify login Incorrect
    assert "Incorrect" in driver.page_source
