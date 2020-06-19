from selene import be
from selene.support.shared.jquery_style import s

from pages.fragments.address_form import AddressForm
from pages.fragments.personal_info_form import PersonalInfoForm


class AccountCreationForm:

    def __init__(self):
        self.container = s("#account-creation_form")

    def _get_personal_info_form(self):
        return PersonalInfoForm(self._get_form_by_number(1))

    def _get_address_form(self):
        return AddressForm(self._get_form_by_number(2))

    def _get_form_by_number(self, number):
        return self.container.ss(".account_creation")[number - 1]

    def registerUser(self):
        self._get_personal_info_form().fill_personal_info()
        self._get_address_form().fill_address_form()
        self.container.s("#submitAccount").click()
        s(".alert.alert-danger").should(be.not_.visible)
        return self

