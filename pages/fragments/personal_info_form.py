from selene.support.shared.jquery_style import s

from models.user import User


class PersonalInfoForm:

    def __init__(self, container):
        self.container = container

    def _set_first_name(self, first_name):
        self.container.s("#customer_firstname").type(first_name)

    def _set_last_name(self, last_name):
        self.container.s("#customer_lastname").type(last_name)

    def _set_password(self, password):
        self.container.s("#passwd").type(password)

    def fill_personal_info(self):
        user = User()
        self._set_first_name(user.first_name_personal)
        self._set_last_name(user.last_name_personal)
        self._set_password(user.password)
        return self
