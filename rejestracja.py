# Rejestracja na atomationpractice.com
# Warunki wstepne
# Konto o podanym mailu nie jest zalozone

# 0. Kliknij Sign In
# 1. Wpisz unikalnego maila
# 2. kliknij "Create account"
# 3. Wybierz tytol (Mr./Mrs.)
# 4. Wpisz imie
# 5. Wpisz nazwisko
# 6. Sprawdz poprawnosc maila
# 7. Wpisz haslo
# 8. Sprawdz poprawnosc imienia
# 9. Sprawdz poprawnosc nazwiska
# 10. Wpisz adres
# 11. Wpisz miasto
# 12. Wpisz stan
# 13. Wpisz kod pocztowy
# 14. Wybierz stan
# 15. Wpisz nr telefonu
# 16. Wpisz alias adresu
# 17. Kliknij Zarejestruj

# Oczekiwany rezultat:
# Brak insormacji o bledach
# (Konto zostalo zalozone)

# Gra do nauki XPATCH - https://topswagcode.com/xpath/
# Dokument pisany przez prowadzcego: http://www.wklejto.pl/txt801730, http://www.wklejto.pl/801730

import unittest
import time

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

email= 'tester@wsb.pl'
gender= 'male'
firstname= 'Blazej'
lastname= 'Anu'
password= '123@abc#'
birth_day= '2'
birth_month= 'January'
birth_year= '2000'

class APRregistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()

    def testCorrectRegestration(self):
        driver = self.driver
        signin = driver.find_element_by_class_name('login')
        signin.click()

        email_input = driver.find_element_by_id('email_create')
        email_input.send_keys(email)

        create_account_btn = driver.find_element_by_id('SubmitCreate')
        create_account_btn.click()

        if gender == 'male':
            driver.find_element_by_id('id_gender1').click()
        if gender == 'female':
            driver.find_element_by_id('id_gender2').click()

        firstname_input = driver.find_element_by_id('customer_firstname')
        firstname_input.send_keys(firstname)

        lastname_input = driver.find_element_by_id('customer_lastname')
        lastname_input.send_keys(lastname)

# Sprawdzanie poprawnosci emaila
        email_fact = driver.find_element_by_id('email').get_attribute('value')
        print (email_fact)
        assert email_fact == email

        password_input = driver.find_element_by_id('passwd')
        password_input.send_keys(password)

# 9. Wpisz date urodzenia
        day = Select(driver.find_element_by_id('days'))
        day.select_by_value(birth_day)
        month = Select(driver.find_element_by_id('months'))
        month.select_by_value('1')
        year = Select(driver.find_element_by_id('years'))
        year.select_by_value(birth_year)

#10 wybieranie poprzez XPATH /sprawdzenie poprawnosci
        name_fact = driver.find_element_by_xpath('//input[@id="customer_firstname"]').get_attribute('value')
        print ("W polu jest imie:", name_fact)
        assert firstname == name_fact
 #przewija strone do danego pola
        #name_fact.location_once_scrolled_into_view

        surname_fact = driver.find_element_by_xpath('//input[@id="customer_lastname"]').get_attribute('value')
        print ("W polu jest nazwisko:", surname_fact)
        assert lastname == surname_fact

if __name__== "__main__":
    unittest.main(verbosity=2)
