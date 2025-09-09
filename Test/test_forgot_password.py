from selenium import webdriver
from Pages.forgot_pass_login_page import LoginPage
from Pages.forgot_pass_page import ForgotPage

# ---------------------------------------------------------
# Test: Verify forgot password flow in the login page
# ---------------------------------------------------------

def test_forgot_password(setup: webdriver):
    driver = setup

    # Step 1: Open the login page URL
    driver.get("https://rahulshettyacademy.com/client/#/auth/login")

    # Step 2: Create LoginPage object and navigate to 'Forgot Password'
    login_page = LoginPage(driver)
    login_page.go_to_forgot_password()

    # Step 3: Create ForgotPage object and complete the password reset
    forgot_page = ForgotPage(driver)
    forgot_page.reset_password()
