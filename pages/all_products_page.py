from .base_page import BasePage
from .locators import AllProductsPageLocators


class AllProductsPage(BasePage):
    def go_to_product_page(self):
        self.click_on_element(*AllProductsPageLocators.PRODUCT_NAME_FROM_ALL_PRODUCTS_PAGE)