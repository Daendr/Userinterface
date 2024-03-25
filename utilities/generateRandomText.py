import random
import string
from py_selenium_auto_core.logging.logger import Logger


class GenerateRandomText:

    @staticmethod
    def generate_random_text(length=10):
        Logger.info("Генерируем случайную строку указанной длины.")
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))


