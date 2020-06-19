from selene import command
from selene.support.shared.jquery_style import s

from pages.fragments.cart_product_fragment import CartProductFragment


class ProductDetailPage:

    def add_to_cart(self):
        s("#add_to_cart").perform(command.js.scroll_into_view).click()
        return CartProductFragment()