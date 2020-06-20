import pytest
from faker import Faker
from selene.api import config, be
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from models.user import User
from pages.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser_ver", action="store", default="")
    parser.addoption("--remote", action="store", default=True)
    parser.addoption("--hub", action="store", default="0.0.0.0")
    parser.addoption("--headless", action="store", default=False)


def get_chrome_options(configuration):
    options = webdriver.ChromeOptions()
    options.headless = configuration["headless"]
    return options


def get_firefox_options(configuration):
    options = webdriver.FirefoxOptions()
    options.headless = configuration["headless"]
    return options


@pytest.fixture
def configuration(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--browser_ver")
    hub = request.config.getoption("--hub")
    headless = False
    remote = False
    if request.config.getoption("--headless"):
        headless = True
    if request.config.getoption("--remote"):
        remote = True

    return {"remote": remote,
            "version": version,
            "browser": browser,
            "headless": headless,
            "hub": hub}


@pytest.fixture(scope='function', autouse=True)
def browser_management(configuration):
    config.base_url = 'http://automationpractice.com'
    config.timeout = 4

    if configuration["remote"]:
        config.driver = create_remote_driver(configuration)
    else:
        create_local_driver(configuration)
    yield
    browser.quit()


def create_remote_driver(configuration):
    if configuration["browser"] == "chrome":
        options = get_chrome_options(configuration)
    else:
        options = get_firefox_options(configuration)

    capabilities = {
        "version": configuration["version"],
        "acceptInsecureCerts": True,
        "enableVNC": True,
        "screenResolution": "1280x1024x24"}

    driver = webdriver.Remote(command_executor=f"http://{configuration['hub']}:4444/wd/hub",
                              options=options,
                              desired_capabilities=capabilities)
    return driver


def create_local_driver(configuration):
    if configuration["browser"] == "chrome":
        options = get_chrome_options(configuration)
        config.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    elif configuration["browser"] == "firefox":
        options = get_firefox_options(configuration)
        config.driver = webdriver.Chrome(GeckoDriverManager().install(), options=options)



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


@pytest.fixture
def logout_user():
    yield
    MainPage().click_logout_button() \
        .signIn_button().should(be.visible)
