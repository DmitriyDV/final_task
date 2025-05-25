from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.go_to_push_add_to_basket()
        self.guest_should_be_see_info_about_what_product_added_to_basket()

    def go_to_push_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def guest_should_be_see_info_about_what_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.INFO_ABOUT_ADD_TO_BASKET)

    def product_in_basket(self):
        in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_ON_PAGE).text
        assert in_basket == product, "Product not in basket"

    def guest_should_be_see_info_about_price_basket(self):
        assert self.is_element_present(*ProductPageLocators.INFO_ABOUT_PRICE), ("Guest don't see"
                                                                                " info about price basket")

    def price_in_basket_equal_price_product(self, price_in_message):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_in_message == product_price, "Price in basket not equals price product"

    def name_in_basket_equal_name_in_message(self, name_in_message):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_ON_PAGE).text
        assert name_in_message == product_price, "Price in basket not equals price product"

    def get_name_product_in_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text

    def get_price_product_in_message(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text

    def get_alert_product_name(self):
        return self.browser.find_elements(*ProductPageLocators.ALERT_PRODUCT_NAME)[0].text

    def get_total_basket_value(self):
        return self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_VALUE).text

    def check_product_name_and_alert_product_name_equals(self, product_name, alert_product_name):
        assert product_name == alert_product_name, 'The names are different'

    def check_price_and_total_basket_value_equals(self, product_price, total_basket_value):
        assert product_price == total_basket_value, 'The prices are different'

