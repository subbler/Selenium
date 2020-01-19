import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleCheck(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_google(self):
        driver = self.driver
        driver.get("https://google.pl")
        enter = driver.find_element_by_name("q")
        enter.send_keys("tester")
        enter.submit()

        results = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"g")))

        print (str(len(results)))
        for result in results:
            print (result.text + "\n")

    def tearDown(self):
	    self.driver.quit()

if __name__ == '__main__':
    unittest.main()
