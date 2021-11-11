from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC


class GithubAdvancedSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.written_language_combo = (By.ID, 'search_language')
        self.amount_stars_input = (By.ID, 'search_stars')
        self.amount_followers = (By.ID, 'search_followers')
        self.license_type_combo = (By.ID, 'search_license')
        self.search_button = (By.XPATH, '//div[@class="d-flex d-md-block"]/button[@type="submit"]')



    def written_language_select_option(self, value):
        Select(wd(self.driver, self.timeout).until(EC.visibility_of_element_located(self.written_language_combo))).select_by_visible_text(value)

    def stars_type(self, value):
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.amount_stars_input)).send_keys(value)

    def followers_type(self, value):
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.amount_followers)).send_keys(value)

    def license_select_option(self, value):
        Select(wd(self.driver, self.timeout).until(EC.visibility_of_element_located(self.license_type_combo))).select_by_visible_text(value)

    def search_button_click(self):
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.search_button)).click()