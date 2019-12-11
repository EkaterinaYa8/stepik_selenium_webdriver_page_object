from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.click_on_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_BUTTON)

    def should_be_product_form(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME),\
            'На странице товара отсутствует элемент с названием товара.'

        product_name = self.element(*ProductPageLocators.PRODUCT_NAME).text

        assert self.is_element_present(*ProductPageLocators.PRODUCT_IMG),\
            f'На странице товара с наименованием: "{product_name}" отсутствует изображение товара.'
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), \
            f'На странице товара с наименованием: "{product_name}" отсутствует элемент со стоимостью товара.'
        assert self.is_element_present(*ProductPageLocators.PRODUCT_STOCK_STATUS), \
            f'На странице товара с наименованием: "{product_name}" отсутствует статус наличия товара.'
        assert self.is_element_present(*ProductPageLocators.PRODUCT_WRITE_REVIEW_BUTTON), \
            f'На странице товара с наименованием: "{product_name}" отсутствует кнопка "Написать отзыв".'

        # если товар в наличии
        if self.is_element_present(*ProductPageLocators.PRODUCT_INSTOCK_AVAILABILITY):
            assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_BUTTON), \
                f'На странице товара с наименованием: "{product_name}" со статусом "в наличии" отсутствует кнопка ' \
                f'"Добавить в корзину".'

            assert self.elements_list(ProductPageLocators.PRODUCT_ADD_TO_WISH_LIST_XPATH) != 0, \
                f'На странице товара с наименованием: "{product_name}" со статусом "в наличии" отсутствует кнопка\n' \
                f'"Добавить к списку желаемого".'

            assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), \
                f'На странице товара с наименованием: "{product_name}" отсутствует элемент размещения заголовка ' \
                f'"Описание товара".'
            assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION_PARAGRAPH), \
                f'На странице товара с наименованием: "{product_name}" отсутствует абзац с описанием товара.'
            assert self.is_element_present(*ProductPageLocators.PRODUCT_INFORMATION), \
                f'На странице товара с наименованием: "{product_name}" отсутствует элемент заголовка ' \
                f'"Информация о товаре".'
            assert self.is_element_present(*ProductPageLocators.PRODUCT_INFORMATION_TABLE), \
                f'На странице товара с наименованием: "{product_name}" отсутствует таблица с информацией о товаре.'
            assert self.elements_list(ProductPageLocators.PRODUCT_INFORMATION_TABLE_ROWS_XPATH) != 0, \
                f'На странице товара с наименованием: "{product_name}" в таблице с информацией о товаре ' \
                f'нет ни одной строки.'
            assert len(self.elements_list(ProductPageLocators.PRODUCT_INFORMATION_TABLE_ROWS_XPATH)) == 7, \
                f'Количество строк в таблице с информацией о товаре с наименованием: "{product_name}" не равно 7.'
            assert self.is_element_present(*ProductPageLocators.PRODUCT_CUSTOMER_REVIEWS), \
                f'На странице товара с наименованием: "{product_name}" отсутствует элемент размещения заголовка ' \
                f'"Отзывы Клиентов".'

    def should_disappeared_success_message(self):
        product_name = self.element(*ProductPageLocators.PRODUCT_NAME).text

        assert self.is_disappeared(*ProductPageLocators.product_alert_msg(self, '1')), \
            f'На странице товара с наименованием: "{product_name}"\n отображается сообщение об успешном добавлении ' \
            f'в корзину, которое должно было исчезнуть.'

    def should_not_be_success_message(self):
        product_name = self.element(*ProductPageLocators.PRODUCT_NAME).text

        assert self.is_not_element_present(*ProductPageLocators.product_alert_msg(self, '1')), \
            f'На странице товара с наименованием: "{product_name}"\n отображается сообщение об успешном добавлении ' \
            f'в корзину, которого быть не должно.'

    def successful_add_to_basket(self):
        product_name = self.element(*ProductPageLocators.PRODUCT_NAME).text
        product_cost = self.element(*ProductPageLocators.PRODUCT_COST).text

        assert len(self.elements_list(ProductPageLocators.PRODUCT_ALERT_MSG_XPATH)) != 0, \
            f'Не отображается сообщение об успешном добавлении товара с наименованием:\n "{product_name}" в корзину ' \
            f'со страницы товара.'

        successful_add_to_basket_msg = self.element(*ProductPageLocators.product_alert_msg(self, '1'))

        assert product_name in successful_add_to_basket_msg.text, \
            f'В сообщении об успешном добавлении товара в корзину:\n{successful_add_to_basket_msg.text}\n' \
            f'или не указано наименование товара, или указано неверно. А должно быть указано наименование:\n' \
            f'"{product_name}".'

        assert len(self.elements_list(ProductPageLocators.PRODUCT_ALERT_MSG_XPATH)) > 1, \
            f'После добавления в корзину товара с наименованием: "{product_name}"\nдолжно быть минимум 2 сообщения, ' \
            f'последнее сообщение должно содержать стоимость корзины.\nА отображается только 1 сообщение.'

        total_basket_msg = self.element(*ProductPageLocators.product_alert_msg(self, str(len(self.elements_list(
            ProductPageLocators.PRODUCT_ALERT_MSG_XPATH)))))
        assert product_cost in total_basket_msg.text, \
            f'В сообщении о стоимости корзины после добавления товара:\n{total_basket_msg.text}\n'\
            f'или не указана стоимость добавленного товара с наименованием:"{product_name}",\nили указана неверно. ' \
            f'А должна быть указана стоимость = {product_cost}.'
