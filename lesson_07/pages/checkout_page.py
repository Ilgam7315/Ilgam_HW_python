from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def fill_shipping_info(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def get_total_amount(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)
        )
        return self.driver.find_element(*self.total_label).text
