import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption('--browser_nm', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: es, fr, ...")

@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_nm")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # Сhrome browser lang settings
        options_chrome = Options()
        service_chrome = Service(ChromeDriverManager().install())
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options_chrome, service=service_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # firefox browser lang settings
        options_firefox = OptionsFirefox()
        service_firefox = FirefoxService(GeckoDriverManager().install())
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options_firefox, service=service_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
