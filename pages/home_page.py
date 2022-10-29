from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class HomePage:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    cart_tab_xpath = "//li[@id='menu-item-20']//a"

    def click_cart_tab(self):
        self.driver.find_element(By.XPATH, HomePage.cart_tab_xpath).click()