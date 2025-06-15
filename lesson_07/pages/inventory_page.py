from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_container = (By.CLASS_NAME, "inventory_list")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.inventory_container)
        )

    def add_product_to_cart(self, product_name):
        add_button_locator = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        )
        self.driver.find_element(*add_button_locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
