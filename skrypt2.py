# Import modulu unitest
import unittest
import time

# Import webdriver
from selenium import webdriver
from time import sleep

# Tworzenie klasy WsbPLCheck dziedziczaca po TestCase z modulu unittest
class WsbPLCheck(unittest.TestCase):

    """Analogia: Przypadek/scenariusz testowy"""

    # Przpadek do kazdego testu (warunki wstepne)
    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(5)

    # Sprzatanie po kazdym tescie
    def tearDown(self):
        self.driver.quit()

    # Wlasciwy test nazwa musi zaczynac sie od slowa test
    def testWsb(self):
        self.driver.get("http://www.wsb.pl")

# Uruchom test jesli uruchamiamy ten plik
if __name__=="__main__":
    unittest.main()
