import pytest
from webdriver_manager.chrome import ChromeDriverManager
from SELENIUM_DEMO_AUTOMATION_TESTS.pages.home_page import HomePage
from SELENIUM_DEMO_AUTOMATION_TESTS.pages.cart_page import CartPage
from SELENIUM_DEMO_AUTOMATION_TESTS.pages.shop_page import ShopPage


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


