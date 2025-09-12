import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import get_logger
from utils.read_json import load_json, get_locator

# Initialize logger for this class/module
logger = get_logger(__name__)

class PracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Load locators from JSON file
        self.locators = load_json("data/practice_page.json")

        # Element locators
        self.radio_button = get_locator(self.locators, "PracticePage", "radio_button")
        self.suggestion_box = get_locator(self.locators, "PracticePage", "suggestion_box")
        self.suggestion_results = get_locator(self.locators, "PracticePage", "suggestion_results")
        self.dropdown = get_locator(self.locators, "PracticePage", "dropdown")
        self.checkbox = get_locator(self.locators, "PracticePage", "checkbox")
        self.open_window_button = get_locator(self.locators, "PracticePage", "open_window_button")
        self.open_tab_button = get_locator(self.locators, "PracticePage", "open_tab_button")
        self.name_input = get_locator(self.locators, "PracticePage", "name_input")
        self.alert_button = get_locator(self.locators, "PracticePage", "alert_button")
        self.confirm_button = get_locator(self.locators, "PracticePage", "confirm_button")
        self.table_one_row = get_locator(self.locators, "PracticePage", "table_one_row")
        self.table_one_instructor_names = get_locator(self.locators, "PracticePage", "table_one_instructor_names")
        self.table_one_course_name = get_locator(self.locators, "PracticePage", "table_one_course_name")
        self.table_one_course_price = get_locator(self.locators, "PracticePage", "table_one_course_price")
        self.table_one_course_row = get_locator(self.locators, "PracticePage", "table_one_row")
        self.hide_btn = get_locator(self.locators, "PracticePage", "hide_btn")
        self.display_text = get_locator(self.locators, "PracticePage", "display_text")
        self.show_btn = get_locator(self.locators, "PracticePage", "show_btn")
        self.table_two_price_cells = get_locator(self.locators, "PracticePage", "table_two_price_cells")
        self.displayed_total_text = get_locator(self.locators, "PracticePage", "displayed_total_text")
        self.mouse_hover = get_locator(self.locators, "PracticePage", "mouse_hover")
        self.top_btn = get_locator(self.locators, "PracticePage", "top_btn")
        self.reload_btn = get_locator(self.locators, "PracticePage", "reload_btn")
        self.contact_email = get_locator(self.locators, "PracticePage", "contact_email")
        self.page_heading = get_locator(self.locators, "PracticePage", "page_heading")

        # Test data from JSON
        self.test_data = self.locators["PracticePage"]
        self.radio_country = self.test_data["suggestion_results"]["test_data"]
        self.dropdown_option = self.test_data["dropdown"]["test_data"]
        self.alert_name = self.test_data["name_input"]["test_data"]
        self.total_amount_expected = int(self.test_data["displayed_total_text"]["test_data"])


    # Scroll to specified Y position
    def scroll(self, length=400):
        self.driver.execute_script(f"scrollTo(0, {length})")

    # Assert current page title
    def verify_page_title(self, expected_title):
        assert self.driver.title == expected_title

    # Click on a radio button
    def select_radio_button(self):
        self.wait.until(EC.element_to_be_clickable(self.radio_button)).click()

    # Select a country from suggestion box dropdown
    def select_country_from_autocomplete(self):
        self.wait.until(EC.visibility_of_element_located(self.suggestion_box)).send_keys(self.radio_country[:3])
        suggestions = self.wait.until(EC.visibility_of_all_elements_located(self.suggestion_results))
        for suggestion in suggestions:
            if suggestion.text.strip() == self.radio_country:
                suggestion.click()
                break

    # Select an option from a dropdown
    def select_dropdown_option(self):
        dropdown_element = self.wait.until(EC.visibility_of_element_located(self.dropdown))
        Select(dropdown_element).select_by_visible_text(self.dropdown_option)

    # Check and assert checkbox
    def check_checkbox(self):
        checkbox_elem = self.wait.until(EC.element_to_be_clickable(self.checkbox))
        checkbox_elem.click()
        assert checkbox_elem.is_selected()

    # Open new window, verify title, close it
    def open_and_verify_new_window(self):
        main_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable(self.open_window_button)).click()
        for win in self.driver.window_handles:
            if win != main_window:
                self.driver.switch_to.window(win)
                self.verify_page_title("QAClick Academy - A Testing Academy to Learn, Earn and Shine")
                self.driver.close()
        self.driver.switch_to.window(main_window)
        self.verify_page_title("Practice Page")

    # Open multiple tabs using Ctrl + Click and verify each tab
    def open_tabs_and_verify(self):
        main_tab = self.driver.current_window_handle
        for _ in range(4):
            ActionChains(self.driver).key_down(Keys.CONTROL).click(
                self.wait.until(EC.element_to_be_clickable(self.open_tab_button))
            ).key_up(Keys.CONTROL).perform()
        for tab in self.driver.window_handles:
            if tab != main_tab:
                self.driver.switch_to.window(tab)
                self.verify_page_title("QAClick Academy - A Testing Academy to Learn, Earn and Shine")
                self.driver.close()
        self.driver.switch_to.window(main_tab)

    # Handle JavaScript alert and verify alert text
    def handle_alert(self):
        self.driver.find_element(*self.name_input).send_keys(self.alert_name)
        self.wait.until(EC.element_to_be_clickable(self.alert_button)).click()
        alert = Alert(self.driver)
        assert self.alert_name in alert.text
        alert.accept()

    # Handle JavaScript confirm box
    def handle_confirm_alert(self):
        self.driver.find_element(*self.name_input).clear()
        self.driver.find_element(*self.name_input).send_keys(self.alert_name)
        self.wait.until(EC.element_to_be_clickable(self.confirm_button)).click()
        confirm = Alert(self.driver)
        assert self.alert_name in confirm.text
        confirm.accept()

    # Verify hide/show functionality of textbox
    def verify_hide_and_show_textbox(self):
        self.scroll(200)
        time.sleep(1)
        textbox = self.driver.find_element(*self.display_text)
        self.driver.find_element(*self.hide_btn).click()
        assert not textbox.is_displayed()
        self.driver.find_element(*self.show_btn).click()
        assert textbox.is_displayed()

    # Return all course table rows
    def get_course_table_rows(self):
        self.scroll(600)
        return self.wait.until(EC.presence_of_all_elements_located(self.table_one_course_row))

    # Assert instructor names match expected
    def verify_instructor_names(self):
        for row in self.get_course_table_rows():
            names = row.find_elements(*self.table_one_instructor_names)
            for name in names:
                assert name.text == "Rahul Shetty"

    # Assert that no course name is empty
    def verify_course_names_not_empty(self):
        for row in self.get_course_table_rows():
            course_names = row.find_elements(*self.table_one_course_name)
            for course in course_names:
                assert course.text.strip() != ""

    # Verify total price of all courses matches expected
    def verify_total_course_amount(self, expected_total=235):
        total = 0
        for row in self.get_course_table_rows():
            prices = row.find_elements(*self.table_one_course_price)
            for price in prices:
                total += int(price.text)
        assert total == expected_total

    # Assert fixed table column cells are not empty
    def verify_fixed_table_column_not_empty(self, column_index: int, column_name: str):
        xpath = f"//div[@class='tableFixHead']/table[@id='product']/tbody/tr/td[{column_index}]"
        cells = self.driver.find_elements(By.XPATH, xpath)
        for cell in cells:
            assert cell.text.strip() != "", f"{column_name} column has empty value"

    # Verify the total price in the fixed header table
    def verify_fixed_header_total_price(self):
        price_cells = self.driver.find_elements(*self.table_two_price_cells)
        total = sum(int(cell.text.strip()) for cell in price_cells)
        displayed_total_text = self.driver.find_element(*self.displayed_total_text).text
        displayed_total = int(displayed_total_text.split(":")[1].strip())
        assert total == self.total_amount_expected == displayed_total

    # Handle mouse hover and interact with hover options
    def handle_hover(self):
        self.scroll(200)
        hover_elem = self.driver.find_element(*self.mouse_hover)
        ActionChains(self.driver).move_to_element(hover_elem).perform()
        self.driver.find_element(*self.top_btn).click()
        assert self.driver.find_element(*self.radio_button)

        self.scroll(1000)
        ActionChains(self.driver).move_to_element(hover_elem).perform()
        assert self.driver.find_element(*self.reload_btn)

    # Switch into iframe, verify content, then return to main page
    def handle_iframe(self):
        self.scroll(1000)
        time.sleep(1)
        self.driver.switch_to.frame("courses-iframe")
        email = self.driver.find_element(*self.contact_email).text
        self.driver.switch_to.default_content()
        assert "rahulshettyacademy.com" in email

    # Verify page heading is correct
    def assert_title(self):
        self.scroll(0)
        heading = self.wait.until(EC.presence_of_element_located(self.page_heading)).text
        assert heading == "Practice Page"

    # Master method to execute full form flow (end-to-end)
    def fill_the_form(self):
        self.verify_page_title("Practice Page")
        self.select_radio_button()
        self.select_country_from_autocomplete()
        self.select_dropdown_option()
        self.check_checkbox()
        self.open_and_verify_new_window()
        self.open_tabs_and_verify()
        self.handle_alert()
        self.handle_confirm_alert()
        self.verify_hide_and_show_textbox()
        self.verify_instructor_names()
        self.verify_course_names_not_empty()
        self.verify_total_course_amount()
        self.verify_fixed_table_column_not_empty(1, "Name")
        self.verify_fixed_table_column_not_empty(2, "Position")
        self.verify_fixed_table_column_not_empty(3, "City")
        self.verify_fixed_table_column_not_empty(4, "Amount")
        self.verify_fixed_header_total_price()
        self.handle_hover()
        self.handle_iframe()
        self.assert_title()
