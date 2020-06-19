import pytest
from faker import Faker
from selene.api import config, be
from selenium import webdriver
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
    config.driver = create_remote_driver()
    config.base_url = "http://automationpractice.com"
    config.timeout = 4


@pytest.fixture
def logout_user():
    yield
    MainPage().click_logout_button() \
        .signIn_button().should(be.visible)


def create_remote_driver():
    options = webdriver.ChromeOptions()

    capabilities = {"browserName": "chrome",
                    "version": "83.0",
                    "acceptInsecureCerts": True,
                    "enableVNC": True,
                    "enableVideo": False,
                    "screenResolution": "1280x1024x24"}

    driver = webdriver.Remote(command_executor="http://172.0.0.1:4444/wd/hub",
                              options=options,
                              desired_capabilities=capabilities)
    return driver
