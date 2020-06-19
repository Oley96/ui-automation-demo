from selene.support.shared.jquery_style import s

from pages.checkout_page import CheckOutPage


class CartProductFragment:

    def __init__(self):
        self.container = s("div[id=layer_cart]")

    def start_checkout(self):
        self.container.s("a[title$='checkout']").click()
        return CheckOutPage()