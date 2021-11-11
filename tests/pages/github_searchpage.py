from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC


class GithubSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.search_textfield = (By.XPATH, '//input[@placeholder="Search GitHub"]')
        self.search_jump_to_first_result = (By.ID, 'jump-to-results')
        self.advanced_search_link = (By.XPATH, '//a[text()="Advanced search"][1]')
        self.repository_found = (By.XPATH, '//h3[contains(text(), "result")]')
        self.respository_name = (By.XPATH, '//div[@class="mt-n1 flex-auto"]/div/div/a')



    def search_button_type(self, value):
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.search_textfield)).send_keys(value)

    def search_jump_to_first_result_click(self):
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.search_jump_to_first_result)).click()

    def advanced_search_link_click(self):
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.advanced_search_link)).click()

    def perform_search(self, value):
        self.search_button_type(value)
        self.search_jump_to_first_result_click()

    def repository_found_get(self):
        return wd(self.driver, self.timeout).until(EC.visibility_of_element_located(self.repository_found)).text

    def repository_name_get(self):
        return wd(self.driver, self.timeout).until(EC.visibility_of_element_located(self.respository_name)).text

    def repository_name_click(self):
        wd(self.driver, self.timeout).until(EC.visibility_of_element_located(self.respository_name)).click()