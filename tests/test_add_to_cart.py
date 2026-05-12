from utils.Credentials import password
from utils.driver_setup import get_driver
from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_search_and_add_to_cart():

    driver = get_driver()

    try:
        home = HomePage(driver)
        product = ProductPage(driver)

        home.open_website(password)

        home.search_product("hydrogen")

        product.open_first_product()

        product.add_to_cart()

        cart_count = product.get_cart_count()

        assert cart_count == "1"

    finally:
        driver.quit()