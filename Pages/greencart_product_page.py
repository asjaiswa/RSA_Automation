from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_json import get_locator, load_json
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # --------------------------
        # Load locators from JSON
        # --------------------------
        self.locators = load_json("data/green_cart.json")
        logger.info("Loaded locators from green_cart.json")

        # Element locators (loaded dynamically from JSON)
        self.product_search = get_locator(self.locators, "ProductPage", "product_search")
        self.matched_products = get_locator(self.locators, "ProductPage", "matched_products")
        self.product_names = get_locator(self.locators, "ProductPage", "product_names")
        self.cart_icon = get_locator(self.locators, "ProductPage", "cart_icon")
        self.proceed_to_checkout = get_locator(self.locators, "ProductPage", "proceed_to_checkout")

    # --------------------------
    # Action: Search and add products to cart
    # --------------------------
    def search_and_add_products(self, text):
        logger.info(f"Searching for products with text: '{text}'")
        self.wait.until(EC.presence_of_element_located(self.product_search)).send_keys(text)

        logger.info("Waiting for matched products to appear")
        products = self.wait.until(EC.presence_of_all_elements_located(self.matched_products))

        logger.info(f"Found {len(products)} matched products. Adding to cart...")
        item_count = 0
        for item in products:
            item_count += 1
            item.find_element(By.XPATH, "div/button").click()
            logger.info(f"Added product #{item_count} to cart")

        assert item_count > 0, "No products were added to the cart."
        logger.info(f"Total products added to cart: {item_count}")

    # --------------------------
    # Action: Navigate to checkout page
    # --------------------------
    def go_to_checkout(self):
        logger.info("Clicking on cart icon")
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

        logger.info("Clicking 'Proceed to Checkout' button")
        self.wait.until(EC.element_to_be_clickable(self.proceed_to_checkout)).click()
        logger.info("Navigated to checkout page")
