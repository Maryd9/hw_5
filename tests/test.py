from selene import browser, have, be

def test_valid_name():
    browser.element('[id=firstName]').should(be.blank).type('Антон')

