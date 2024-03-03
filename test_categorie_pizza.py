import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Categorie_pizza(unittest.TestCase):
    Select_pizza = (By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")



    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_categorie_pizza(self):
        self.chrome.find_element(*self.Select_pizza).click()







