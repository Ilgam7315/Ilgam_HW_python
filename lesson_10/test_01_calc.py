import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Ilgam_HW_python.lesson_10.calc_page import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка работы калькулятора с задержкой")
@allure.description("Тест проверяет корректность вычислений при установленной задержке")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver):
    calc_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calc_page.open()

    with allure.step("Установить задержку 45 секунд"):
        calc_page.set_delay(45)

    with allure.step("Выполнить операцию 7 + 8 ="):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

    with allure.step("Дождаться результата и проверить его"):
        calc_page.wait_for_result(46, "15")

        with allure.step("Проверить, что результат равен 15"):
            assert calc_page.get_result() == "15", "Ожидаемый результат: 15"
