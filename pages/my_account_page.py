from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    my_account_title_xpath = "//h1[@class='entry-title'][text()='My account']"

    def check_if_my_account_title_is_displayed(self):
        return self.driver.find_element(By.XPATH, MyAccountPage.my_account_title_xpath).is_displayed()


