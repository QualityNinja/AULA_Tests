import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Test")
class TestProfileFeature(BaseTest):

    @allure.title('testеest')
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_creation(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_enter_button()
        #self.home_page.is_opened() - изминения на вебе - убрали страницу
        #self.home_page.click_requests_button() - изминения на вебе - убрали страницу
        self.requests_page.click_create_request()
        self.requests_page.pop_up_sccept()
        self.requests_page.house()
        self.requests_page.change_house()
        self.requests_page.click_apartment_type()
        self.requests_page.change_apartment()
        self.requests_page.apartment_number()
        self.requests_page.enter_phone()
        self.requests_page.add_user_phone()
        self.requests_page.porch_field()
        self.requests_page.change_porch()
        self.requests_page.change_floor()
        self.requests_page.change_category()
        self.requests_page.enter_description()
        self.requests_page.click_create()
