from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.read_json import get_locator, load_json
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class ProtoCommercePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # ----------------------------------------------
        # Load locators and test data from JSON file
        # ----------------------------------------------
        self.data = load_json("data/smartphone_shop.json")
        logger.info("Loaded locators and test data from smartphone_shop.json")

        # Assign locators from JSON
        self.page_title = get_locator(self.data, "ProtoCommercePage", "page_title")
        self.all_phone = get_locator(self.data, "ProtoCommercePage", "all_phone")
        self.nav_link_btn = get_locator(self.data, "ProtoCommercePage", "nav_link_btn")

        # Load expected test data
        self.actual_phone_list = self.data["ProtoCommercePage"]["test_data"]["expected_phone_list"]

    # ----------------------------------------------------
    # Action: Select specific phones and proceed to cart
    # ----------------------------------------------------
    def test_add_phone_to_cart(self):
        logger.info("Starting 'add phone to cart' test")

        # Step 1: Assert page heading
        page_heading = self.wait.until(
            EC.visibility_of(self.driver.find_element(*self.page_title))
        ).text
        expected_heading = self.data["ProtoCommercePage"]["page_title"]["locator_value"]
        logger.info(f"Verifying page title: Expected='{expected_heading}', Actual='{page_heading}'")
        assert page_heading == expected_heading

        # Step 2: Scroll down to view all phone cards
        self.driver.execute_script("window.scrollTo(0, 300)")
        logger.info("Scrolled down to view all phone cards")

        # Step 3: Wait for all phone cards
        all_phone_elements = self.wait.until(EC.visibility_of_all_elements_located(self.all_phone))
        logger.info(f"Found {len(all_phone_elements)} phone cards on the page")

        expected_phone_list = []

        # Step 4: Loop through phone cards
        for phone in all_phone_elements:
            phone_name = phone.find_element(By.XPATH, "div/div/h4/a").text
            expected_phone_list.append(phone_name)
            logger.info(f"Found phone: {phone_name}")

            # Step 5: Add specific phones to cart
            if phone_name in ["iphone X", "Samsung Note 8"]:
                logger.info(f"Adding '{phone_name}' to cart")
                phone.find_element(By.XPATH, "div/div/button").click()

        # Step 6: Scroll back to top and click on Checkout
        self.driver.execute_script("window.scrollTo(0, 0)")
        self.driver.find_element(*self.nav_link_btn).click()
        logger.info("Clicked on 'Checkout' button")

        # Step 7: Verify phone list
        logger.info(f"Verifying selected phone list: Expected={self.actual_phone_list}, Actual={expected_phone_list}")
        assert self.actual_phone_list == expected_phone_list
        logger.info("'Add phone to cart' test completed successfully")
