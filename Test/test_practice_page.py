from selenium import webdriver
from Pages.practice_page import PracticePage

# ---------------------------------------------------------
# Test: Complete Practice Page Automation
# 1. Fill the form with radio buttons, dropdowns, checkboxes
# 2. Handle alerts, windows, tabs, iframes, and table validations
# ---------------------------------------------------------
def test_practice_page(setup: webdriver):
    driver = setup

    # Step 1: Open the Practice Page URL
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    # Step 2: Create PracticePage object and perform all actions
    practice_page = PracticePage(driver)
    practice_page.fill_the_form()
