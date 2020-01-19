import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

email= 'tester@wsb.pl'
gender= 'male'
firstname= 'Jan'
lastname= 'Kowalski'
password= '123@abc#'
birth_day= '2'
birth_month= 'January'
birth_year= '2000'
address= '2630 Cahaba Rd'
city= 'Birmingham'
postal_code= '35223'
Country= 'United States'
Mphone= '0011223344'

class APRregistration(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://automationpractice.com/index.php')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def testNoName(self):
        driver = self.driver
        signin = driver.find_element_by_class_name('login')
        signin.click()

        email_input = driver.find_element_by_id('email_create')
        email_input.send_keys(email)

        create_account_btn = driver.find_element_by_id('SubmitCreate')
        create_account_btn.click()

    if gender == "male":
            driver.find_element_by_id("id_gender1").click()
    elif gender=="female":
            driver.find_element_by_id("id_gender2").click()

    driver.find_element_by_id("customer_lastname").send_keys(surname)

    driver.find_element_by_id("passwd").send_keys(password)

    day =  Select(driver.find_element_by_id("days"))
    day.select_by_value(birth_day)
    month =  Select(driver.find_element_by_id("months"))
    month.select_by_visible_text(birth_month)
    year =  Select(driver.find_element_by_id("years"))
    year.select_by_value(birth_year)

    driver.find_element_by_id('address1').send_keys(address)

    driver.find_element_by_id('city').send_keys(city)

    driver.find_element_by_id('postcode').send_keys(postcode)

    state_select =  Select(driver.find_element_by_id("id_state"))
    state_select.select_by_visible_text("Alabama")

    driver.find_element_by_id('phone_mobile').send_keys(Mphone)

    al = driver.find_element_by_id('alias')
    al.clear()
    al.send_keys(alias)

    driver.find_element_by_id('submitAccount').click()

    #Pobieranie bledow

    errors = driver.find_elements_by_xpath('//div[@class="alert alert-danger"]/ol')
    assert len(errors) == 1
    error_text = errors[0].get_attribute('innerText')
    assert errors[0].is_displayed()
    assert "firstname is required" in error_text

if __name__ == "__main__":
    unittest.main(verbosity=2)
