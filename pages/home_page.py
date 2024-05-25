import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    PAGE_URL = Links.HOME_PAGE
    REUESTS_BUTTON = ('xpath', '//*[@id="head-menu-2"]')

    @allure.step("Click on Requests page")
    def click_requests_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REUESTS_BUTTON)).click()
