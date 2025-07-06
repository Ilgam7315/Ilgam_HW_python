from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Класс для работы со страницей товаров."""

    def __init__(self, driver):
        """
        Инициализация экземпляра класса.

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def wait_for_page_load(self) -> None:
        """Ожидает загрузки страницы товаров."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет указанный товар в корзину.

        :param product_name: str - название товара
        """
        add_button_locator = (By.XPATH,
                              f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.driver.find_element(*add_button_locator).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        self.driver.find_element(*self.cart_icon).click()
