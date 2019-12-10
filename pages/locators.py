from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')


class LoginPageLocators():
    LOGIN_USER_NAME = (By.XPATH, '//input[@name="login-username"]')
    LOGIN_PASSWORD = (By.XPATH, '//input[@name="login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')

    REGISTRATION_USER_NAME = (By.XPATH, '//input[@name="registration-email"]')
    REGISTRATION_PASSWORD_1 = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTRATION_PASSWORD_2 = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
