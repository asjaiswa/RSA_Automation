from selenium import webdriver
from Pages.proto_commerce_form_page import PromoPage
from Pages.smartphone_shop_login_page import LoginPageToShop

# ---------------------------------------------------------
# Test: Verify Promo Page Form Submission
# 1. Login to the smartphone shop
# 2. Fill promo form with user details
# 3. Submit the form and verify success message
# ---------------------------------------------------------
def test_promo(setup: webdriver):
    driver = setup

    # Step 1: Open the login page URL
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Step 2: Perform successful login using LoginPageToShop
    login_page = LoginPageToShop(driver)
    login_page.test_successful_login()

    # Step 3: Fill the promo form and submit
    promo_page = PromoPage(driver)
    promo_page.fill_form(
        username=promo_page.name,
        email=promo_page.email,
        password=promo_page.password,
        gender_value=promo_page.test_gender,
        dob_value=promo_page.dob
    )
    promo_page.submit_form()

    # Step 4: Verify success message after form submission
    assert "Success" in promo_page.get_success_message()
