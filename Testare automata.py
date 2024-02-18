import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture(scope="module")
def browser():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    yield chrome
    chrome.quit()

def test_log_in(browser):
    # Open the webpage
    browser.get("https://www.fabiopizza.ro/")
    sleep(2)
    logare = browser.find_element(By.XPATH, "//a[@class='topbar-but but-account js-login-splash-trigger' and @title='Conectare']")
    logare.click()
    sleep(3)
    mail = browser.find_element(By.XPATH, "//input[@id='login_email']")
    mail.send_keys("andy.alexandrub@gmail.com")
    selectparola = browser.find_element(By.XPATH, "//input[@id='login_password']")
    selectparola.send_keys("fab123pizza321")
    sleep(2)
    connect = browser.find_element(By.XPATH, "//button[@id='login_do']")
    connect.click()
    sleep(2)

def test_categorie_pizza(browser):
    browser.get("https://www.fabiopizza.ro/")
    sleep(2)
    selectpizza = browser.find_element(By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    selectpizza.click()
    sleep(3)

def test_filtru_nu_carne(browser):
    browser.get("https://www.fabiopizza.ro/")
    sleep(5)
    selectpizza = browser.find_element(By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    selectpizza.click()
    filtrunucarne = browser.find_element(By.XPATH, "//button[@class='searchtag tag-vegy js-searchtag']")
    filtrunucarne.click()
    sleep(3)

def test_accesam_pizza(browser):
    browser.get("https://www.fabiopizza.ro/")
    sleep(5)
    selectpizza = browser.find_element(By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    selectpizza.click()
    selectpizza = browser.find_element(By.XPATH, "//div[contains(@class, 'plist-item-wrapper') and .//p[@class='plist_title' and contains(text(), 'Pizza Abruzzo')]]")
    selectpizza.click()
    sleep(3)

def test_scoatem_ingredient(browser):
    browser.get("https://www.fabiopizza.ro/")
    sleep(5)
    selectpizza = browser.find_element(By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    selectpizza.click()
    selectpizzanew = browser.find_element(By.XPATH, "//div[contains(@class, 'plist-item-wrapper') and .//p[@class='plist_title' and contains(text(), 'Pizza Abruzzo')]]")
    selectpizzanew.click()
    sleep(3)
    scoatem_ingredient = browser.find_element(By.XPATH, '//*[@id="frm_atc"]/div/div[2]/div[2]/div[2]/div/ul/li[1]/button')
    scoatem_ingredient.click()
    sleep(5)

def test_timp_estimativ(browser):
     browser.get("https://www.fabiopizza.ro/")
     sleep(3)
     contact = browser.find_element(By.XPATH, '/html/body/div[2]/aside/div[1]/div/a')
     contact.click()
     sleep(3)

def test_contact(browser):
     browser.get("https://www.fabiopizza.ro/")
     sleep(3)
     meniu = browser.find_element(By.XPATH, "/html/body/div[2]/aside/div[2]/div[2]/div[2]/a[2]")
     meniu.click()
     sleep(3)
     contact = browser.find_element(By.XPATH, '//*[@id="menu_11"]/li[8]/a')
     contact.click()

def test_info_utile(browser):
    browser.get("https://www.fabiopizza.ro/")
    sleep(3)
    meniu = browser.find_element(By.XPATH, "/html/body/div[2]/aside/div[2]/div[2]/div[2]/a[2]")
    meniu.click()
    sleep(3)
    infoutile = browser.find_element(By.XPATH, '//*[@id="menu_11"]/li[5]/a')
    infoutile.click()

def test_search(browser):
    browser.get("https://www.fabiopizza.ro/")
    sleep(3)
    search = browser.find_element(By.XPATH, '//*[@id="search_key_"]')
    search.send_keys("vegan")
    sleep(2)
    clicksearch = browser.find_element(By.XPATH, '//*[@id="search_button_"]')
    clicksearch.click()
    sleep(2)

def test_homepage(browser):
    browser.get("https://www.fabiopizza.ro/")
    sleep(3)
    desert = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/nav/ul/li[5]/a')
    desert.click()
    sleep(2)
    homepage = browser.find_element(By.XPATH, '/html/body/div[2]/aside/a/img')
    homepage.click()
    sleep(2)

if __name__ == "__main__":
    pytest.main()


