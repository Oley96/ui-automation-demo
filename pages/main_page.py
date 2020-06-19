from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from pages.authentication_page import AuthenticationPage
from pages.fragments.categories_fragment import CategoriesFragment
from pages.fragments.search_fragment import SearchFragment


class MainPage:

    def open(self):
        browser.open("/")
        # browser.driver.maximize_window()
        return self

    def click_signIn_button(self):
        self.signIn_button().click()
        return AuthenticationPage()

    def open_category_page(self, category):
        return CategoriesFragment().get_category_with(category)

    def open_product_page_from_search(self, query):
        return SearchFragment().get_first_product_from_search(query)

    def click_logout_button(self):
        s(".logout").click()
        return AuthenticationPage()

    def signIn_button(self):
        return s(".login")
