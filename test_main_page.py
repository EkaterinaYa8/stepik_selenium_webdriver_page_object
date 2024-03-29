import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.all_products_page import AllProductsPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_main_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket_message()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_all_products_page()
        all_products_page = AllProductsPage(browser, browser.current_url)
        all_products_page.go_to_product_page()
        product_page = ProductPage(browser, browser.current_url)
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket_message()
