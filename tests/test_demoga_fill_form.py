import os

from selene import browser, be, have


def test_demoga_fill_form(set_demoga):
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Alesha')
    browser.element('#lastName').click().type('Bigd')
    browser.element('#userEmail').click().type('mf666@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').click().type('0123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="1"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1955"]').click()
    browser.element('.react-datepicker__day--012').click()
    browser.element("#subjectsInput").click().type("Arts").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('files/ava.jpg'))
    browser.element('#currentAddress').click().type('Heaven')
    browser.element('#react-select-3-input').type('Uttar Pradesh').click().press_enter()
    browser.element('#react-select-4-input').type('Agra').click().press_enter()
    browser.element('#submit').click()

    browser.element('.modal-content').should(be.visible)
    browser.element('.table').all('td:nth-of-type(2)').should(have.texts(
        'Alesha Bigd',
        'mf666@gmail.com',
        'Male',
        '0123456789',
        '12 February,1955',
        'Arts',
        'Sports, Reading',
        'ava.jpg',
        'Heaven',
        'Uttar Pradesh Agra'))
