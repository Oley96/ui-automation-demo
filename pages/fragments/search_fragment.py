from selene.support.shared.jquery_style import s, ss

from pages.product_detail_page import ProductDetailPage


class SearchFragment:

    def __init__(self):
        self.container = s("#searchbox")

    def _search_product(self, query):
        self.container.s(".search_query").clear().type(query)
        # self.container.s("[name='submit_search']").click()

    def get_first_product_from_search(self, query):
        self._search_product(query)
        ss(".ac_results > ul > li").first.hover().click()
        return ProductDetailPage()