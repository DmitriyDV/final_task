from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CURRENT_LANGUAGE = (By.CSS_SELECTOR, 'select[name="language"] option[selected]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    CONTINUE_SHOPPING_TEXT = (By.CSS_SELECTOR, '#content_inner p a')


class LoginPageLocators:
    REGISTRATION_EMAIL_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_FORM_BUTTON = (By.XPATH, "//*[@value='Register']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_LINK = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM_BUTTON = (By.XPATH, "//*[@value='Log In']")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div p")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")  # кнопка "добавить в корзину"
    INFO_ABOUT_ADD_TO_BASKET = (By.CSS_SELECTOR,
                                "div div.alert:nth-child(1)")  # сообщение об успешном добавлении товара с именем товара в начале
    PRODUCT_ON_PAGE = (By.CSS_SELECTOR, "div h1")  # имя товара в карточке
    PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div div.alert:nth-child(1) strong")  # имя товара в сообщении
    INFO_ABOUT_PRICE = (By.CSS_SELECTOR, "div div.alert:nth-child(3)")  # сообщение о цене товара
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "div div.alert:nth-child(3) strong")  # цена товара в сообщении
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div p.price_color")  # цена товара в карточке
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success .alertinner strong ')
    TOTAL_BASKET_VALUE = (By.CSS_SELECTOR, '.alert-info .alertinner strong ')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
