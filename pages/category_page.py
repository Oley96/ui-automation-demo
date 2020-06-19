from selene import command
from selene.support.shared.jquery_style import ss, s

from pages.fragments.product_fragment import ProductFragment


class CategoryPage:

    def get_first_product(self):
        return ProductFragment(self.get_product_list()[0].hover())

    def get_product_list(self):
        container = s("ul[class='product_list grid row']").perform(command.js.scroll_into_view)
        return container.ss("div[class='product-container']")