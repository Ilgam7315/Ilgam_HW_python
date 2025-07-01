from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver):
        """
        Инициализация экземпляра класса.

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def wait_for_page_load(self) -> None:
        """Ожидает загрузки страницы корзины."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart_list"))
        )

    def click_checkout(self) -> None:
        """Начинает оформление заказа."""
        self.driver.find_element(*self.checkout_button).click()
