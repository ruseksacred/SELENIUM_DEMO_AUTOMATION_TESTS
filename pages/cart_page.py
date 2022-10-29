from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    return_to_shop_button_xpath = "//p[@class='return-to-shop']//a"
    cart_title_text_xpath = "//div[@class='entry-header-inner']//h1"

    def click_return_to_shop_button(self):
        self.driver.find_element(By.XPATH, CartPage.return_to_shop_button_xpath).click()

    def check_if_cart_title_is_displayed(self):
        return self.driver.find_element(By.XPATH, CartPage.cart_title_text_xpath).is_displayed()

