import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1366
    browser.config.window_height = 768

    yield

    browser.quit()