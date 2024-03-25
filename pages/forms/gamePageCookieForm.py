from selenium.webdriver.common.by import By
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.label import Label


class GamePageCookieForm(Form):
    _accept_cookies = Label(
        Locator(By.CLASS_NAME, "button--transparent"),
        "accept_cookies")

    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "button--transparent"),
            "accept_cookies")

    def click_accept_cookies(self):
        self._accept_cookies.click()
