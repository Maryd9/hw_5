import os
from selene import browser, have, be


def test_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Антон')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('test@user.ru')
    browser.element('.custom-control-label').click()
    browser.element('#userNumber').type('8985874996')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__day--015').click()
    browser.element('#subjectsInput').set_value('English').press_enter()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture.png'))
    browser.element('#currentAddress').type(
        '009728, Псковская область, город Шаховская, пл. Славы, 78')
    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()

    browser.element('#submit').click()

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