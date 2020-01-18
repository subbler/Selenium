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

import unittest
import time

from selenium import webdriver
import time

email= 'tester@wsb.pl'
gender= 'male'

class APRregistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()
# testu

    def testCorrectRegestration(self):
        driver = self.driver
        signin = driver.find_element_by_class_name("login")
        signin.click()

        email_input = driver.find_element_by_id('email_create')
        email_input.send_keys(email)

        create_account_btn = driver.find_element_by_id('SubmitCreate')
        create_account_btn.click()

        if gender == 'male':
            driver.find_element_by_id('id_gender1').click()
        if gender == 'female':
            driver.find_element_by_id('id_gender2').click()

        time.sleep(3)

if __name__== "__main__":
    unittest.main()
