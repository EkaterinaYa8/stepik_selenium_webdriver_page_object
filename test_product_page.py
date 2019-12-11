import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from time import time


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture
    def setup(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(str(time()) + '@testmail.org', 'truepassw')
        login_page.should_be_login_icon()

    def test_user_cant_see_success_message(self, setup, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, setup, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_form()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.successful_add_to_basket()

    def test_guest_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_form()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.successful_add_to_basket()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket_message()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()



