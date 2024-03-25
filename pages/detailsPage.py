from selenium.webdriver.common.by import By
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class GamePageDetails(Form):
    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "personal-details__td-label"),
            "Проверка для GamePageDetails - это 3 карточка",
        )
