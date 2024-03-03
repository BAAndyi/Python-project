import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_login(unittest.TestCase):
    Logare = (By.XPATH, "//a[@class='topbar-but but-account js-login-splash-trigger' and @title='Conectare']")
    Mail = (By.XPATH, "//input[@id='login_email']")
    Select_parola = (By.XPATH, "//input[@id='login_password']")
    Connect = (By.XPATH, "//button[@id='login_do']")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_log_in(self):
        self.chrome.find_element(*self.Logare).click()
        self.chrome.find_element(*self.Mail).send_keys("andy.alexandrub@gmail.com")
        self.chrome.find_element(*self.Select_parola).send_keys("fab123pizza321")
        self.chrome.find_element(*self.Connect).click()



