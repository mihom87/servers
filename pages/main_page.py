from pages.base_page import BasePage
from utils.webdriver import WebDriver


class MainPage(BasePage):
    """
    Класс для главной страницы.
    """

    path = "/"

    def __init__(self, driver: WebDriver):
        """
        Инициализация главной страницы.

        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver, self.__class__.path)
