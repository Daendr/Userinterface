import pytest
from py_selenium_auto_core.logging.logger import Logger
from pages.startPage import StartPage
from pages.loginPage import GamePageLogin
from pages.interestsPage import GamePageInterests
from pages.detailsPage import GamePageDetails
from pages.forms.gamePageCookieForm import GamePageCookieForm
from pages.forms.gamePageHelpForm import GamePageHelpForm
from pages.forms.gamePageTimer import GamePageTimer
from utilities.generateRandomText import GenerateRandomText


class TestUserinterface:

    @staticmethod
    @pytest.mark.test_Registration
    def test_registration():
        Logger.info("Шаг 1. Перейти на домашнюю страницу.")
        start_page = StartPage()
        assert start_page.state.is_displayed(), "Стартовая страница не отображена"

        Logger.info("Шаг 2. Кликнуть по ссылке HERE для перехода на следующую страницу.")
        start_page.click_here_link()
        game_page_1 = GamePageLogin()
        assert game_page_1.state.is_displayed(), "Cтраница 1 карточки игры не отображена"

        Logger.info("Шаг 3. Введите случайные действующий пароль,"
                    " адрес электронной почты,примите условия пользования и нажмите кнопку 'Next'")
        email = GenerateRandomText.generate_random_text(10)
        game_page_1.send_email(email)
        game_page_1.send_domain(GenerateRandomText.generate_random_text(5))
        game_page_1.send_password(email)
        game_page_1.click_open_dropdown()
        game_page_1.select_high_domain()
        game_page_1.agree_terms()
        game_page_1.click_next_btn()
        game_page_2 = GamePageInterests()
        assert game_page_2.state.is_displayed(), "Cтраница 2 карточки игры не отображена"

        Logger.info("Шаг 4. Выберите 3 случайных интереса, загрузите изображение, нажмите кнопку 'Next'")
        game_page_2.upload_photo()
        game_page_2.click_checkbox_unselectall()
        game_page_2.click_random_checkbox(3)
        game_page_2.click_next_btn_second_card()
        game_page_3 = GamePageDetails()
        assert game_page_3.state.is_displayed(), "Cтраница 3 карточки игры не отображена"

    @staticmethod
    @pytest.mark.test_Hide_help_form
    def test_hide_help_form():
        Logger.info("Шаг 1. Перейти на домашнюю страницу.")
        start_page = StartPage()
        assert start_page.state.is_displayed(), "Стартовая страница не отображена"

        Logger.info("2. Скрыть форму помощи.")
        start_page.click_here_link()
        game_page_help_form = GamePageHelpForm()
        game_page_help_form.click_hide_help_form_btn()
        assert game_page_help_form.state.wait_for_not_displayed(),\
            "Форма не исчезла после нажатия кнопки cкрыть форму помощи"

    @staticmethod
    @pytest.mark.test_Accept_cookies
    def test_accept_cookies():
        Logger.info("Шаг 1. Перейти на домашнюю страницу.")
        start_page = StartPage()
        assert start_page.state.is_displayed(), "Стартовая страница не отображена"

        Logger.info("2. Принять cookies.")
        start_page.click_here_link()
        game_page_cookie_form = GamePageCookieForm()
        game_page_cookie_form.click_accept_cookies()
        assert game_page_cookie_form.state.wait_for_not_displayed(),\
            "Форма не исчезла после нажатия на кнопку 'No, really no'"

    @staticmethod
    @pytest.mark.test_Timer
    def test_timer():
        Logger.info("Шаг 1. Перейти на домашнюю страницу.")
        start_page = StartPage()
        start_page.click_here_link()

        game_page_timer = GamePageTimer()
        assert game_page_timer.timer_starts_with_zero(), "Время на таймере отличается от 00:00:00"
