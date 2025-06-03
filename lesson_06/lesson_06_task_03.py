from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Шаг 1: Переход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Шаг 2: Ожидание загрузки всех картинок
waiter = WebDriverWait(driver, 20)
waiter.until(
    EC.invisibility_of_element_located((By.CSS_SELECTOR, "#spinner"))
)

# Шаг 3: Получение значение атрибута src 3-й картинки
image_container = driver.find_element(By.ID, "image-container")
images = image_container.find_elements(By.TAG_NAME, "img")
third_image_src = images[2].get_attribute("src")

# Шаг 4: Вывод значения в консоль
print("Атрибут src третьей картинки:", third_image_src)

# Завершение работы драйвера
driver.quit()
