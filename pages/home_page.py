from utils.Credentials import base_url
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    SEARCH_LENS = (By.XPATH,"//summary[@aria-label='Search']//span")
    SEARCH_BOX = (By.XPATH, "//input[@id='Search-In-Modal']")
    SEARCH_BUTTON = (By.XPATH, "//button[@aria-label='Search']")
    SEARCH_RESULTS = (By.XPATH, "//a[contains(@id,'CardLink') and contains(@href,'products')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_website(self, password):
        self.driver.get(base_url)
        try:
            password_field = self.driver.find_element(By.XPATH, "//input[@id='password']")
            password_field.send_keys(password)
            enter_btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Enter']")
            enter_btn.click()
        except:
            pass  # Password not required or already entered

    def search_product(self, product_name):
        search_lense = self.wait.until(EC.element_to_be_clickable(self.SEARCH_LENS))
        search_lense.click()
        search_box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        search_box.clear()
        search_box.send_keys(product_name)
        search_btn = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_btn.click()
        self.wait.until(EC.url_contains("/search"))
        self.wait.until(EC.presence_of_all_elements_located(self.SEARCH_RESULTS))
