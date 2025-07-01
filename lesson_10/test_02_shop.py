import pytest
import allure
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


@allure.title("Проверка процесса покупки в интернет-магазине")
@allure.description("Тест проверяет полный процесс покупки: авторизацию, добавление товаров, оформление заказа")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_sauce_demo_purchase(driver):
    # Инициализация страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть сайт и авторизоваться"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Ожидание загрузки главной страницы"):
        inventory_page.wait_for_page_load()

    with allure.step("Добавление товаров в корзину"):
        products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for product in products:
            inventory_page.add_product_to_cart(product)

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()
        cart_page.wait_for_page_load()

    with allure.step("Начало оформления заказа"):
        cart_page.click_checkout()

    with allure.step("Заполнение формы доставки"):
        checkout_page.fill_shipping_info("Иван", "Иванов", "123456")

    with allure.step("Проверка итоговой суммы заказа"):
        total_text = checkout_page.get_total_amount()
        with allure.step(f"Убедиться, что итоговая сумма равна $58.29 (фактическая: {total_text})"):
            assert total_text == "Total: $58.29", \
                f"Ожидаемая сумма: $58.29, Фактическая: {total_text}"
