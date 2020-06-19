from selene.support.shared.jquery_style import s

from pages.authentication_page import AuthenticationPage


class NavigationFragment:

    def __init__(self):
        self.container = s(".nav")

    def sign_in_button(self):
        return self.container.s(".login")

    def click_signIn_button(self):
        self.sign_in_button().click()
        return AuthenticationPage()

    def logout_button(self):
        return self.container.s(".logout")

    def click_logout_button(self):
        self.logout_button().click()
        return AuthenticationPage()

