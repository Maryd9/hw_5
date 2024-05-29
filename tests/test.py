import os
from selene import browser, have, be


def test_form(browser_managment):
    browser.element('[id=firstName]').should(be.blank).type('Антон')
    browser.element('[id=lastName]').should(be.blank).type('Иванов')
    browser.element('[id=userEmail]').should(be.blank).type('test@user.ru')
    browser.element('[class=custom-control-label]').should(have.text('Male')).click()
    browser.element('[id=userNumber]').should(be.blank).type('8985874996')
    browser.element('[id=dateOfBirthInput]').click()
    browser.element('.react-datepicker__day--015').click()
    browser.element('[id=subjectsInput]').should(be.blank).set_value('English').press_enter()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('[id=uploadPicture]').send_keys(os.path.abspath('picture.png'))
    browser.element('[id=currentAddress]').should(be.blank).type(
        '009728, Псковская область, город Шаховская, пл. Славы, 78')
    browser.element('[id=state]').click().element('#react-select-3-option-2').click()
    browser.element('[id=city]').click().element('#react-select-4-option-1').click()

    browser.element('[id=submit]').click()

    browser.element(".modal-content").element("table").all("tr").all("td").even.should(
        have.exact_texts(
            "Антон Иванов",
            "test@user.ru",
            "Male",
            "8985874996",
            "15 May,2024",
            "English",
            "Music",
            "picture.png",
            "009728, Псковская область, город Шаховская, пл. Славы, 78",
            "Haryana Panipat"
        ))
