from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_json import load_json, get_locator
from utils.logger import get_logger  # Import logger

# Initialize logger
logger = get_logger(__name__)

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # --------------------------
        # Load locators from JSON
        # --------------------------
        self.locators = load_json("data/green_cart.json")
        logger.info("Loaded locators from green_cart.json")

        # Element locators
        self.promo_code_input = get_locator(self.locators, "CheckoutPage", "promo_code_input")
        self.apply_promo_btn = get_locator(self.locators, "CheckoutPage", "apply_promo_btn")
        self.promo_info = get_locator(self.locators, "CheckoutPage", "promo_info")
        self.total_amount = get_locator(self.locators, "CheckoutPage", "total_amount")
        self.discount_amount = get_locator(self.locators, "CheckoutPage", "discount_amount")
        self.place_order_ele = get_locator(self.locators, "CheckoutPage", "place_order_ele")

    # --------------------------
    # Action: Apply promo code
    # --------------------------
    def apply_promo_code(self, code):
        logger.info(f"Applying promo code: {code}")

        # Step 1: Enter the promo code
        self.wait.until(EC.presence_of_element_located(self.promo_code_input)).send_keys(code)
        logger.info("Entered promo code")

        # Step 2: Click on the "Apply" button
        self.wait.until(EC.element_to_be_clickable(self.apply_promo_btn)).click()
        logger.info("Clicked 'Apply' button")

        # Step 3: Wait for promo confirmation and validate text
        promo_text = self.wait.until(EC.presence_of_element_located(self.promo_info)).text
        logger.info(f"Promo confirmation text: '{promo_text}'")
        assert promo_text == "Code applied ..!", (
            f"Expected promo confirmation 'Code applied ..!' but got '{promo_text}'"
        )
        logger.info("Promo code applied successfully")

    # --------------------------
    # Action: Verify discount applied
    # --------------------------
    def verify_discount_applied(self):
        total = float(self.driver.find_element(*self.total_amount).text)
        discount = float(self.driver.find_element(*self.discount_amount).text)
        logger.info(f"Total amount: {total}, Discount amount: {discount}")

        assert total > discount, (
            f"Expected discount < total. Got total: {total}, discount: {discount}"
        )
        logger.info("Discount applied successfully and verified")

    # --------------------------
    # Action: Place the order
    # --------------------------
    def place_order(self):
        logger.info("Clicking 'Place Order' button")
        self.wait.until(EC.element_to_be_clickable(self.place_order_ele)).click()

        confirmation_ele = self.wait.until(
            EC.visibility_of(self.driver.find_element(By.CSS_SELECTOR, "div label"))
        )
        assert confirmation_ele, "Expected confirmation element after placing the order was not visible"
        logger.info("Order placed successfully and confirmation element is visible")
