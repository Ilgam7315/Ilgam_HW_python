import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calc_page import CalculatorPage  # Импорт созданного класса


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # Инициализация Page Object
    calc_page = CalculatorPage(driver)

    # Шаг 1: Открыть страницу калькулятора
    calc_page.open()

    # Шаг 2: Установить задержку 45 секунд
    calc_page.set_delay(45)

    # Шаг 3: Выполнить операцию 7 + 8 =
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    # Шаг 4: Дождаться результата и проверить его
    calc_page.wait_for_result(46, "15")
    assert calc_page.get_result() == "15"
