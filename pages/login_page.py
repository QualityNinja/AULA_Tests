import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

# Селекторы


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    LOGIN_FIELD = ('xpath', '//input[@name="phone"]')
    PASSWORD_FIELD = ('xpath', '//input[@name="password"]')
    ENTER_BUTTON = ('xpath', '//*[@id="submit"]')

# Проверки с явным ожиданием

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_FIELD)).send_keys(login)

    @allure.step("Password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click enter button")
    def click_enter_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_BUTTON)).click()
