from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    ADD_TO_CART_BUTTON = (By.NAME, "add")
    CART_COUNT = (By.XPATH, "//input[@id='Drawer-quantity-1']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_first_product(self):
        all_products = (By.XPATH,"//a[contains(@id,'CardLink') and contains(@href,'products')]")
        product_list = self.driver.find_elements(*all_products)
        first_product = self.wait.until(EC.element_to_be_clickable(product_list[0]))
        first_product.click()

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()

    def get_cart_count(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_COUNT)).get_attribute("value")