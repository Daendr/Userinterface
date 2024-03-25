import locale
import os
import random
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto.elements.label import Label
from selenium.webdriver.common.by import By
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.button import Button
import subprocess


class GamePageInterests(Form):

    _upload_button = Button(
        Locator(By.CLASS_NAME, "avatar-and-interests__upload-button"),
        "upload_button")
    _next_button_2_card = Button(
        Locator(By.XPATH, "//*[contains(text(), 'Next')]"),
        "next_button_2_card")
    _check_boxes_elements = Label(
        Locator(By.XPATH, "//label[not(contains(@for, 'select'))]"),
        "_check_boxes_elements")
    _unselectall_checkbox = Button(
        Locator(By.XPATH, f'//*[@for="interest_unselectall"]'),
        "_unselectall_checkboxes")

    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "avatar-and-interests__title"),
            "Проверка для GamePageInterests - вторая карточка",
        )

    def upload_photo(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        system_language, _ = locale.getdefaultlocale()
        if system_language.startswith('ru'):
            autoit_script = "choose_file_ru.exe"
        else:
            autoit_script = "choose_file_en.exe"
        autoit_exe_path = os.path.join(script_dir, "../utilities", autoit_script)
        self._upload_button.click()
        subprocess.run([autoit_exe_path])

    def click_checkbox_unselectall(self):
        self._unselectall_checkbox.click()

    def click_random_checkbox(self, num):
        checkbox_list = BrowserServices.Instance.browser.driver.find_elements(
            By.XPATH, self._check_boxes_elements.locator.value)
        for _ in range(num):
            random_checkbox = random.choice(checkbox_list)
            random_checkbox.click()
            checkbox_list.remove(random_checkbox)

    def click_next_btn_second_card(self):
        self._next_button_2_card.click()
