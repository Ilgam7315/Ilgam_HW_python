from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver):
        """
        Инициализация экземпляра класса.

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает значение задержки вычислений.

        :param seconds: int - время задержки в секундах
        """
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(str(seconds))

    def click_button(self, button_text: str) -> None:
        """
        Нажимает указанную кнопку калькулятора.

        :param button_text: str - текст на кнопке (например, '7', '+', '=')
        """
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*locator).click()

    def get_result(self) -> str:
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str - текст результата
        """
        return self.driver.find_element(*self.screen).text

    def wait_for_result(self, timeout: int, expected_text: str) -> None:
        """
        Ожидает появления указанного текста в результате.

        :param timeout: int - максимальное время ожидания в секундах
        :param expected_text: str - ожидаемый текст результата
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, expected_text)
        )
