import random
import string
from py_selenium_auto_core.logging.logger import Logger


class PasswordGenerator:

    @staticmethod
    def generate_password(email):
        Logger.info("Генерируем пароль с учетом указанных требований.")
        first_char = email[0].upper()
        second_char = random.choice(string.digits)
        cyrillic_char = random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        password = first_char + second_char + cyrillic_char + email[3:]
        return password
