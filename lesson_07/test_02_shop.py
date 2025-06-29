import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_sauce_demo_purchase(driver):
    # Инициализация страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Шаг 1: Открыть сайт и авторизоваться
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Шаг 2: Ожидание загрузки главной страницы
    inventory_page.wait_for_page_load()

    # Шаг 3: Добавление товаров в корзину
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for product in products:
        inventory_page.add_product_to_cart(product)

    # Шаг 4: Переход в корзину
    inventory_page.go_to_cart()
    cart_page.wait_for_page_load()

    # Шаг 5: Начало оформления заказа
    cart_page.click_checkout()

    # Шаг 6: Заполнение формы доставки
    checkout_page.fill_shipping_info("Иван", "Иванов", "123456")

    # Шаг 7: Получение и проверка итоговой суммы
    total_text = checkout_page.get_total_amount()
    assert total_text == "Total: $58.29", f"Ожидаемая сумма: $58.29, Фактическая: {total_text}"
