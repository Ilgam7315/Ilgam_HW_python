import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_sauce_demo_purchase(driver):
    # Шаг 1: Открыть сайт магазина
    driver.get("https://www.saucedemo.com/")

    # Шаг 2: Авторизация
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()

    # Проверка успешной авторизации
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Шаг 3: Добавление товаров в корзину
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        # Формируем локатор для кнопки "Add to cart" конкретного товара
        add_to_cart_btn = driver.find_element(
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        )
        add_to_cart_btn.click()

    # Шаг 4: Переход в корзину
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    # Проверка перехода в корзину
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cart_contents_container"))
    )

    # Шаг 5: Нажатие Checkout
    checkout_btn = driver.find_element(By.ID, "checkout")
    checkout_btn.click()

    # Шаг 6: Заполнение формы и нажатие кнопки "Continue"
    first_name = driver.find_element(By.ID, "first-name")
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")
    continue_btn = driver.find_element(By.ID, "continue")

    first_name.send_keys("Иван")
    last_name.send_keys("Иванов")
    postal_code.send_keys("123456")
    continue_btn.click()

    # Шаг 7: Проверка итоговой суммы
    # Ожидаем загрузки страницы с итогами
    total_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    total_text = total_element.text
    assert total_text == "Total: $58.29", f"Ожидаемая сумма: $58.29, Фактическая: {total_text}"
