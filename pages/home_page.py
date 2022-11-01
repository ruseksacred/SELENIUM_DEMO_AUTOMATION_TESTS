from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    cart_tab_xpath = "//li[@id='menu-item-20']//a"
    shop_tab_xpath = "//li[@id='menu-item-21']//a"
    my_account_tab_xpath = "//li[@id='menu-item-22']//a"
    shop_button_xpath = "//div[@class='sek-module-inner']//a"

    def click_cart_tab(self):
        self.driver.find_element(By.XPATH, HomePage.cart_tab_xpath).click()

    def click_shop_tab(self):
        self.driver.find_element(By.XPATH, HomePage.shop_tab_xpath).click()

    def click_my_account_tab(self):
        self.driver.find_element(By.XPATH, HomePage.my_account_tab_xpath).click()

    def click_shop_button(self):
        self.driver.find_element(By.XPATH, HomePage.shop_button_xpath).click()


