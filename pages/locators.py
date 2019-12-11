from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_USER_NAME = (By.XPATH, '//input[@name="login-username"]')
    LOGIN_PASSWORD = (By.XPATH, '//input[@name="login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')

    REGISTRATION_USER_NAME = (By.XPATH, '//input[@name="registration-email"]')
    REGISTRATION_PASSWORD_1 = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTRATION_PASSWORD_2 = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_IMG = (By.XPATH, '//div[@class="col-sm-6"]/div/div/div/div/img')
    PRODUCT_COST = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    PRODUCT_STOCK_STATUS = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[2]')
    PRODUCT_INSTOCK_AVAILABILITY = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="instock availability"]')
    PRODUCT_WRITE_REVIEW_BUTTON = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[3]/a')
    PRODUCT_ADD_TO_BASKET_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/button[@type="submit"]')
    PRODUCT_ADD_TO_WISH_LIST = (By.XPATH, '//button[@class="btn btn-lg btn-wishlist"]')
    PRODUCT_DESCRIPTION = (By.XPATH, '//div[@id="product_description"]')
    PRODUCT_DESCRIPTION_PARAGRAPH = (By.XPATH, '//article[@class="product_page"]/p')
    PRODUCT_INFORMATION = (By.XPATH, '//article[@class="product_page"]/div[3]')
    PRODUCT_INFORMATION_TABLE = (By.XPATH, '//table[@class="table table-striped"]')

    PRODUCT_INFORMATION_TABLE_ROWS_XPATH = '//table[@class="table table-striped"]/tbody/tr'

    PRODUCT_CUSTOMER_REVIEWS = (By.XPATH, '//section/div[@id="reviews"]')

    PRODUCT_ALERT_MSG_XPATH = '//div[@class="alertinner "]'

    def product_alert_msg(self, num):
        return (By.XPATH, f'//div[{num}]/div[@class="alertinner "]')

    def product_cost_from_alert_msg(self, num):
        return (By.XPATH, f'//div[{num}]/div[@class="alertinner "]/p/strong')
