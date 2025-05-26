from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

flash_message = driver.find_element(By.CLASS_NAME, "flash.success")
message_text = flash_message.text.split("\n")[1]
print("Сообщение системы:", message_text)

driver.quit()
