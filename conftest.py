import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="write language")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    browser = webdriver.Chrome(options=options)
    print(f"\nstart browser for test with language:{language_name}..")
    yield browser
    print("\nquit browser..")
    browser.quit()
    
    
