from selenium.webdriver.common.by import By


class LoginPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver):
        """
        Инициализация экземпляра класса.

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self) -> None:
        """Открывает страницу авторизации."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию с указанными учетными данными.

        :param username: str - имя пользователя
        :param password: str - пароль
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
