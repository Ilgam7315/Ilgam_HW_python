from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        # Устанавливает значение задержки в секундах
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(str(seconds))

    def click_button(self, button_text):
        # Нажимает кнопку с указанным текстом
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*locator).click()

    def get_result(self):
        # Возвращает текущий текст из поля результата
        return self.driver.find_element(*self.screen).text

    def wait_for_result(self, timeout, expected_text):
        # Ожидает появления указанного текста в результате
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, expected_text)
        )
