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
        all_products = (By.XPATH, "//a[contains(@id,'CardLink') and contains(@href,'products')]")
        self.wait.until(EC.visibility_of_any_elements_located(all_products))
        first_product = self.wait.until(EC.element_to_be_clickable(all_products))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_product)
        first_product.click()

    def add_to_cart(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
        add_button.click()

    def get_cart_count(self):
        return self.wait.until(lambda driver: (
            driver.find_element(*self.CART_COUNT).get_attribute("value") or False
        ))
