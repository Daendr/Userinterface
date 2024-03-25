from selenium.webdriver.common.by import By
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.button import Button


class GamePageHelpForm(Form):
    hide_help_form_btn = Button(
        Locator(By.CLASS_NAME, "help-form__send-to-bottom-button"),
        "help_form_btn")

    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "help-form__send-to-bottom-button"),
            "help_form_btn")

    def click_hide_help_form_btn(self):
        self.hide_help_form_btn.click()
