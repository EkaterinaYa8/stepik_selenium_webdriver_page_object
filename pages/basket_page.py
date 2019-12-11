from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_ROW), \
            'В корзине не должно быть ни одного товара, т.к. товары не были добавлены.'

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MSG), \
            'В корзине должно отображаться сообщение, что корзина пуста.'
