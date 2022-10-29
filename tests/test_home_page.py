import pytest
from webdriver_manager.chrome import ChromeDriverManager
from SELENIUM_DEMO_AUTOMATION_TESTS.pages.home_page import HomePage
from SELENIUM_DEMO_AUTOMATION_TESTS.pages.cart_page import CartPage


@pytest.mark.usefixtures("setup")
class TestHomePage:

    def test_click_cart_tab(self):
        home_page = HomePage(self.driver)
        cart_page = CartPage(self.driver)
        home_page.click_cart_tab()
        assert cart_page.check_if_cart_title_is_displayed()
