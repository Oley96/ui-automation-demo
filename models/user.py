import random
import time


class User:

    def __init__(self):
        self.first_name_personal = "John"
        self.last_name_personal = "Doe"
        self.password = "123456789"

        self.first_name = "John"
        self.last_name = "Doe"
        self.address = "Shevchenka 17d"
        self.city = "Kiev"
        self.state = "Alaska"
        self.post_code = "12345"
        self.mobile_phone = "0970000000"
        self.alias = str(round(time.time(), 10)) + str(round(random.random(), 3))