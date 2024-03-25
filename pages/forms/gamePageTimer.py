from selenium.webdriver.common.by import By
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.label import Label


class GamePageTimer(Form):
    _timer = Label(
        Locator(By.CLASS_NAME, "timer--center"),
        "timer")

    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "timer--center"),
            "timer")

    def timer_starts_with_zero(self):
        timer_text = self._timer.get_element().text
        return timer_text.startswith("00:00:00")
