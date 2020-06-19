from selene.support.by import text
from selene.support.shared.jquery_style import s

from pages.category_page import CategoryPage


class CategoriesFragment:

    def __init__(self):
        self.container = s("ul[class*='sf-menu clearfix menu-content']")

    def get_category_with(self, category):
        self.container.s(f"[title={category}]").click()
        return CategoryPage()