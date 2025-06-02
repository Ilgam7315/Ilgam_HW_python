from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация драйвера с автоматической установкой chromedriver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)  # поместим метод перед переходом на сайт (сразу настраиваем драйвер на ожидание)

# Шаг 1: Переход на сайт
driver.get("http://uitestingplayground.com/ajax")

# Шаг 2: Нажатие синей кнопки
button = driver.find_element(By.ID, "ajaxButton")
button.click()

# Шаг 3: Получение текста из зеленой плашки
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# Шаг 4: Вывод значения в консоль
print(txt)

# Завершение работы драйвера
driver.quit()
