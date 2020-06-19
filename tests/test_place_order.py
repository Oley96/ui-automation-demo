from selene import have
from pages.main_page import MainPage


def test_can_place_order_from_category_page(register_user):
    MainPage().open() \
        .open_category_page("Women") \
        .get_first_product() \
        .add_to_cart() \
        .start_checkout() \
        .proceed_checkout_steps() \
        .confirm_with_bank_wire() \
        .bank_wire_status().should(have.text("Your order on My Store is complete."))


def test_can_place_order_from_search(register_user):
    MainPage().open() \
        .open_product_page_from_search("shirt") \
        .add_to_cart() \
        .start_checkout() \
        .proceed_checkout_steps() \
        .confirm_with_pay_check() \
        .pay_check_status().should(have.text("Your order on My Store is complete."))
