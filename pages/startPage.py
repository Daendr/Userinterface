from selenium.webdriver.common.by import By
from py_selenium_auto.elements.link import Link
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class StartPage(Form):
    _here_link = Link(
        Locator(By.CLASS_NAME, "start__link"),
        "HERE",
    )

    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "start__paragraph"),
            "Start Page",
        )

    def click_here_link(self):
        self._here_link.click()
