import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_shopping(unittest.TestCase):
    Select_pizza = (By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    Filtru_nu_carne = (By.XPATH, "//button[@class='searchtag tag-vegy js-searchtag']")
    Contact = (By.XPATH, '/html/body/div[2]/aside/div[1]/div/a')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_filtru_nu_carne(self):
       self.chrome.find_element(*self.Select_pizza).click()
       self.chrome.find_element(*self.Filtru_nu_carne).click()

    def test_timp_estimativ(self):
       self.chrome.find_element(*self.Contact).click()
