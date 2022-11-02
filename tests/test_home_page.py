import pytest
from webdriver_manager.chrome import ChromeDriverManager
from SELENIUM_DEMO_AUTOMATION_TESTS.pages.home_page import HomePage
from SELENIUM_DEMO_AUTOMATION_TESTS.pages.cart_page import CartPage
from SELENIUM_DEMO_AUTOMATION_TESTS.pages.shop_page import ShopPage
from SELENIUM_DEMO_AUTOMATION_TESTS.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestHomePage:

    def test_click_cart_tab(self):
        home_page = HomePage(self.driver)
        cart_page = CartPage(self.driver)
        home_page.click_cart_tab()
        assert cart_page.check_if_cart_title_is_displayed()

    def test_click_shop_tab(self):
        home_page = HomePage(self.driver)
        shop_page = ShopPage(self.driver)
        home_page.click_shop_tab()
        assert shop_page.check_if_shop_page_title_is_displayed()

    def test_click_my_account_tab(self):
        home_page = HomePage(self.driver)
        my_account_page = MyAccountPage(self.driver)
        home_page.click_my_account_tab()
        assert my_account_page.check_if_my_account_title_is_displayed()

    def test_click_shop_button(self):
        home_page = HomePage(self.driver)
        shop_page = ShopPage(self.driver)
        home_page.click_shop_button()
        assert shop_page.check_if_shop_page_title_is_displayed()

    def test_click_title_home_page_return_to_home_page(self):
        home_page = HomePage(self.driver)
        shop_page = ShopPage(self.driver)
        home_page.click_shop_button()
        shop_page.click_main_page_title()
        assert self.driver.current_url == "http://seleniumdemo.com/"







