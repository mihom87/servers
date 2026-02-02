from pages.base_page import BasePage
from utils.webdriver import WebDriver


class MainPage(BasePage):
    """
    Класс для главной страницы.
    """

    path = "/"

    def __init__(self, driver: WebDriver, timeout: int = 30000):
        """
        Инициализация главной страницы.

        Args:
            driver: Экземпляр WebDriver
            timeout: Время ожидания в миллисекундах (implicit wait для всей системы)
        """
        super().__init__(driver, self.__class__.path, timeout)
