import pytest
from selene import browser


@pytest.fixture(scope="function")
def set_demoga():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 800
    browser.config.window_width = 400
    browser.config.timeout = 4.0

    yield
    browser.quit()
