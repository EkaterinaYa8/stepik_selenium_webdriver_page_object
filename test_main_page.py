
def test_guest_can_go_to_login_page(browser, link, current_language):
    browser.get(link)
    browser.implicitly_wait(10)

    # Поиск и клик по надписи-ссылке 'Войти или зарегистрироваться'
    login_registration_link = browser.find_element_by_xpath(
        '//ul[@class="nav navbar-nav navbar-right"]/li/a[@id="login_link"]')
    login_registration_link.click()
    browser.implicitly_wait(10)

    assert len(browser.find_elements_by_xpath('//div[@class="page_inner"]/ul[@class="breadcrumb"]')) != 0, \
        'На странице \"Войти или зарегистрироваться\" отсутствует путь до текущего раздела.'

    assert len(browser.find_elements_by_xpath('//input[@name="login-username"]')) != 0, \
                'На странице \"Войти или зарегистрироваться\" отсутствует поле для ввода email в форме авторизации.'

    assert len(browser.find_elements_by_xpath('//input[@name="login-password"]')) != 0, \
        'На странице \"Войти или зарегистрироваться\" отсутствует поле для ввода пароля в форме авторизации.'

    assert len(browser.find_elements_by_xpath('//button[@name="login_submit"]')) != 0, \
        'На странице \"Войти или зарегистрироваться\" отсутствует кнопка для входа пользователя.'

    assert len(browser.find_elements_by_xpath('//input[@name="registration-email"]')) != 0, \
       'На странице \"Войти или зарегистрироваться\" отсутствует поле для ввода email в форме регистрации.'

    assert len(browser.find_elements_by_xpath('//input[@name="registration-password1"]')) != 0, \
        'На странице \"Войти или зарегистрироваться\" отсутствует поле для ввода пароля в форме регистрации.'

    assert len(browser.find_elements_by_xpath('//input[@name="registration-password2"]')) != 0, \
        'На странице \"Войти или зарегистрироваться\" отсутствует поле для повторного ввода пароля в форме регистрации.'

    assert len(browser.find_elements_by_xpath('//button[@name="registration_submit"]')) != 0, \
        'На странице \"Войти или зарегистрироваться\" отсутствует кнопка подтверждения регистрации.'
