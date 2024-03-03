import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_search(unittest.TestCase):
    Search = (By.XPATH, '//*[@id="search_key_"]')
    Click_search = (By.XPATH, '//*[@id="search_button_"]')


    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_search(self):
        self.chrome.find_element(*self.Search).click()
        self.chrome.find_element(*self.Click_search).click()
