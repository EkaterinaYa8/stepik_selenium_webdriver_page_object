from .base_page import BasePage
from .locators import LoginPageLocators
import re


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_in_url_list = re.findall('accounts/(\w+)', self.browser.current_url)
        print(login_in_url_list)

        assert len(login_in_url_list) == 1, \
            'URL страницы входа и регистрации должен содержать в конце login.' \
            'Ошибка парсинга URL на наличие "login" после "accounts/", возможно, URL был изменён.'

        assert login_in_url_list[0] == 'login', 'URL страницы входа и регистрации должен содержать в конце login.'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER_NAME), \
            'На странице "Войти или зарегистрироваться" отсутствует поле для ввода email в форме авторизации.'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            'На странице "Войти или зарегистрироваться" отсутствует поле для ввода пароля в форме авторизации.'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), \
            'На странице "Войти или зарегистрироваться" отсутствует кнопка для входа пользователя.'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USER_NAME), \
            'На странице "Войти или зарегистрироваться" отсутствует поле для ввода email в форме регистрации.'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1), \
            'На странице "Войти или зарегистрироваться" отсутствует поле для ввода пароля в форме регистрации.'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2), \
            'На странице "Войти или зарегистрироваться" отсутствует поле для повторного ввода пароля в форме регистрации.'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), \
            'На странице "Войти или зарегистрироваться" отсутствует кнопка подтверждения регистрации.'
