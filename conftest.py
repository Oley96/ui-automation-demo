import pytest
from faker import Faker
from selene.support.conditions import be
from selene.support.shared import browser

from models.user import User
from pages.main_page import MainPage


@pytest.fixture
def fake():
    return Faker()


@pytest.fixture
def register_user(fake):
    email = fake.email()
    MainPage().open() \
        .click_signIn_button() \
        .start_create_account(email) \
        .registerUser()
    return email, User().password


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 4
    browser.config.base_url = 'http://automationpractice.com'
    yield
    browser.quit()

@pytest.fixture
def logout_user():
    yield
    MainPage().click_logout_button() \
        .signIn_button().should(be.visible)
