from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация драйвера с автоматической установкой chromedriver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Шаг 1: Переход на сайт
driver.get("http://uitestingplayground.com/textinput")

# Шаг 2: Ввод текста  "Skypro" в поле
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

# Шаг 3: Нажатие на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

# Шаг 4: Получение текста кнопки и вывод текста в консоль
button_text = button.text
print(button_text)

# Завершение работы драйвера
driver.quit()
