from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver):
        """
        Инициализация экземпляра класса.

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_shipping_info(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Заполняет информацию о доставке.

        :param first_name: str - имя покупателя
        :param last_name: str - фамилия покупателя
        :param zip_code: str - почтовый индекс
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_amount(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: str - текст с итоговой суммой
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)
        )
        return self.driver.find_element(*self.total_label).text
