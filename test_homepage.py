import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_homepage(unittest.TestCase):
    Select_pizza_link = (By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    Select_specific_pizza = (By.XPATH, "//div[contains(@class, 'plist-item-wrapper') and .//p[@class='plist_title' and contains(text(), 'Pizza Abruzzo')]]")
    Desert = (By.XPATH, '/html/body/div[2]/div[3]/div/nav/ul/li[5]/a')
    Homepage = (By.XPATH, '/html/body/div[2]/aside/a/img')
    Meniu = (By.XPATH, "/html/body/div[2]/aside/div[2]/div[2]/div[2]/a[2]")
    Info_utile = (By.XPATH, '//*[@id="menu_11"]/li[5]/a')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_accesam_pizza(self):
        self.chrome.find_element(*self.Select_pizza_link).click()
        self.chrome.find_element(*self.Select_specific_pizza).click()

    def test_homepage(self):
        self.chrome.find_element(*self.Desert).click()
        self.chrome.find_element(*self.Homepage).click()

    def test_info_utile(self):
        self.chrome.find_element(*self.Meniu).click()
        self.chrome.find_element(*self.Info_utile).click()