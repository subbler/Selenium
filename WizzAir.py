import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

firstname= 'Janusz'
lastname= 'Kowalski'
gender= 'M'
phone= '111222333'
valid_country= 'Polska'

class GoogleCheck(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_WizzAir(self):
        driver = self.driver
        driver.get("https://wizzair.com/pl-pl#/")
        zaloguj_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()

        sleep(3)

        rejestracja_btn = driver.find_element_by_xpath('//button[text()=" Rejestracja "]')
        rejestracja_btn.click()

        sleep(2)

        firstname_input = driver.find_element_by_xpath('//input[@data-test="registrationmodal-first-name-input"]')
        firstname_input.send_keys(firstname)

        lastname_input = driver.find_element_by_xpath('//input[@data-test="registrationmodal-last-name-input"]')
        lastname_input.send_keys(lastname)

        if gender == 'M':
            m = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            firstname_input.click()
            m.click()
        else:
            f = driver.find_element_by_xpath('//label[@for="register-gender-female"]')
            f.click()

        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        countries = country_to_choose.find_elements_by_tag_name("label")
        for label in countries:
            option = label.find_element_by_tag_name('strong')
            if option.get_attribute("innerText") == valid_country:
                option.location_once_scrolled_into_view
                option.click()
            break

        driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]').click()

        driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]').click()

        error_notices = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        assert len(visible_error_notices) == 1
        error_text = visible_error_notices[0].get_attribute("innerText")
        assert error_text == "Nieprawidłowy adres e-mail"

        sleep(4)

if __name__== "__main__":
    unittest.main(verbosity=2)
