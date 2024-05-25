import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.requests_page import RequestsPage
from config.data import Data


class BaseTest:
    login_page: LoginPage
    home_page: HomePage
    requests_page: RequestsPage
    data: Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.data = Data()
        request.cls.home_page = HomePage(driver)
        request.cls.requests_page = RequestsPage(driver)
