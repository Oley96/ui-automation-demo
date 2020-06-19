from selene.support.shared.jquery_style import s

from pages.fragments.cart_product_fragment import CartProductFragment


class ProductFragment:

    def __init__(self, container):
        self.container = container


    def add_to_cart(self):
        self.container.s("a[class*='add_to_cart']").click()
        return CartProductFragment()