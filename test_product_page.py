import pytest
from .pages.product_page import ProductPage


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_push_add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.guest_should_be_see_info_about_what_product_added_to_basket()
#     page.product_in_basket()
#     page.guest_should_be_see_info_about_price_basket()
#     price_in_message = page.get_price_product_in_message()
#     page.price_in_basket_equal_price_product(price_in_message)
#     name_in_message = page.get_name_product_in_message()
#     page.name_in_basket_equal_name_in_message(name_in_message)

# @pytest.mark.parametrize('link',
#                              ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                               pytest.param(
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   marks=pytest.mark.xfail),
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_push_add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.guest_should_be_see_info_about_what_product_added_to_basket()
#     page.product_in_basket()
#     page.guest_should_be_see_info_about_price_basket()
#     product_name = page.get_name_product_in_message()
#     alert_product_name = page.get_alert_product_name()
#     product_price = page.get_price_product_in_message()
#     total_basket_value = page.get_total_basket_value()
#     page.check_price_and_total_basket_value_equals(product_price, total_basket_value)
#     page.check_product_name_and_alert_product_name_equals(product_name,alert_product_name)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_success_message_disappeared()
