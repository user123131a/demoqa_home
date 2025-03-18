from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestCheckText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_footer_text(self):
        driver = self.driver
        driver.get("https://demoqa.com/")
        footer_text = driver.find_element(By.CSS_SELECTOR, "footer").text
        expected_footer_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
        self.assertEqual(footer_text, expected_footer_text)

    def test_center_text(self):
        driver = self.driver
        driver.get('https://demoqa.com')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[1]/h1')))
        center_text = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/h1').text
        expected_center_text = 'Please select an item from left to start practice.'
        self.assertEqual(center_text, expected_center_text)

if __name__ == '__main__':
    unittest.main()
