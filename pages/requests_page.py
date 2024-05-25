import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RequestsPage(BasePage):
    PAGE_URL = Links.REQUEST_PAGE
    ADD_REQUEST_BUTTON = ('xpath', '//*[@id="top"]/div[1]/div[1]/div[1]/button[1]')
    POP_UP_ACCEPT = ('xpath', '//button/span[text()=" Ок "]')
    HOUSE = ('xpath', '(//div[@role="combobox"])[3]')
    CHOICE_HOUSE = ('xpath', '//div[text()="улица Сыганак, 60/1"]')
    APARTMENT_TYPE = ('xpath', '(//div/div[@role="button"])[3]')
    APARTMENT_TYPE_CHOICE = ('xpath', '//div/div[text()="Квартира"]')
    APARTMENT_NUMBER = ('xpath', '(//div//div//input[@required])[3]')
    USER_PHONE = ('xpath', '(//div//div//input[@required])[4]')
    ADD_USER_PHONE = ('xpath', '(//div//div//input[@placeholder="+7-"])[3]')
    PORCH = ('xpath', '(//div/div[@role="button"])[4]')
    PORCH_CHOICE = ('xpath', '//div[text()="1"]')
    FLOOR = ('xpath', '(//div//div//input[@required])[6]')
    CATEGORY = ('xpath', '//span[text()=" Сантехника "]')
    DESCRIPTION = ('xpath', '//div/textarea')
    UPLOAD_FILE = ('xpath', '//input[@type="file"]')
    CREATE_BUTTON = ('xpath', '//span[text()=" Создать "]')
    REFRESH = ('xpath', '(//span[@class="v-btn__content"])[5]')
    VIEW_REQUEST = ('xpath', '(//tr)[3]')

    @allure.step("Click add request button")
    def click_create_request(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_REQUEST_BUTTON)).click()

    @allure.step("Accept popup")
    def pop_up_sccept(self):
        self.wait.until(EC.element_to_be_clickable(self.POP_UP_ACCEPT)).click()

    @allure.step("Click house filed")
    def house(self):
        self.wait.until(EC.element_to_be_clickable(self.HOUSE)).click()

    @allure.step("Change house")
    def change_house(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOICE_HOUSE)).click()

    @allure.step("Click apartment field")
    def click_apartment_type(self):
        self.wait.until(EC.element_to_be_clickable(self.APARTMENT_TYPE)).click()

    @allure.step("Change apartment field")
    def change_apartment(self):
        self.wait.until(EC.element_to_be_clickable(self.APARTMENT_TYPE_CHOICE)).click()

    @allure.step("Change apartment number")
    def apartment_number(self):
        self.wait.until(EC.element_to_be_clickable(self.APARTMENT_NUMBER)).send_keys("24")

    @allure.step("Enter user phone")
    def enter_phone(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_PHONE)).send_keys("1234567890")

    @allure.step("Enter add user phone")
    def add_user_phone(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_USER_PHONE)).send_keys("0987654321")

    @allure.step("Click porch field")
    def porch_field(self):
        self.wait.until(EC.element_to_be_clickable(self.PORCH)).click()

    @allure.step("Change porch")
    def change_porch(self):
        self.wait.until(EC.element_to_be_clickable(self.PORCH_CHOICE)).click()

    @allure.step("Change floor")
    def change_floor(self):
        self.wait.until(EC.element_to_be_clickable(self.FLOOR)).send_keys("24")

    @allure.step("Change category")
    def change_category(self):
        self.wait.until(EC.element_to_be_clickable(self.CATEGORY)).click()

    @allure.step("Enter description")
    def enter_description(self):
        self.wait.until(EC.element_to_be_clickable(self.DESCRIPTION)).send_keys("Паша - автотестирование процесса "
                                                                                "заявок - создание новой заявки")

    @allure.step("Click create button")
    def click_create(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()
