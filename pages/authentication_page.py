from selene.support.conditions import be
from selene.support.shared.jquery_style import s

from pages.fragments.account_creation_form import AccountCreationForm
from pages.my_account_page import MyAccountPage


class AuthenticationPage:

    def start_create_account(self, email):
        account_form = s("#create-account_form")
        account_form.s("input[name='email_create']").type(email)
        account_form.s("#SubmitCreate").click()
        return AccountCreationForm()

    def login_with(self, email, password):
        container = s("#login_form")
        container.s("#email").type(email)
        container.s("#passwd").type(password)
        container.s("#SubmitLogin").click()
        s(".alert.alert-danger").should(be.not_.visible)
        return MyAccountPage()
