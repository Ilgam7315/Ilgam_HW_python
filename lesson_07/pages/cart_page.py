from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_container = (By.ID, "cart_contents_container")
        self.checkout_button = (By.ID, "checkout")

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.cart_container)
        )

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
