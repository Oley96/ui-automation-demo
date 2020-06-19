import random
import time

from selene import by

from models.user import User


class AddressForm:

    def __init__(self, container):
        self.container = container

    def _set_first_name(self, first_name):
        self.container.s("#firstname").type(first_name)

    def _set_last_name(self, last_name):
        self.container.s("#lastname").type(last_name)

    def _set_address_first_line(self, address):
        self.container.s("#address1").type(address)

    def _set_city(self, city):
        self.container.s("#city").type(city)

    def _set_post_code(self, post_code):
        self.container.s("#postcode").type(post_code)

    def _set_mobile_phone(self, phone):
        self.container.s("#phone_mobile").type(phone)

    def _set_alias(self, alias):
        self.container.s("#alias").clear().type(alias)

    def _set_state(self, state):
        self.container.s("select[name='id_state']").s(by.text(state)).click()

    def fill_address_form(self):

        self._set_first_name(User().first_name)
        self._set_last_name(User().last_name)
        self._set_address_first_line(User().address)
        self._set_city(User().city)
        self._set_state(User().state)
        self._set_post_code(User().post_code)
        self._set_mobile_phone(User().mobile_phone)
        self._set_alias(User().alias)