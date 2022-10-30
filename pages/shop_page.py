from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    shop_page_title_xpath = "//h1[@class='woocommerce-products-header__title page-title']"

    def check_if_shop_page_title_is_displayed(self):
        return self.driver.find_element(By.XPATH, ShopPage.shop_page_title_xpath).is_displayed()