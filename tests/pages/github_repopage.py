from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC


class GithubRepoPage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.readme = (By.XPATH, '//article')

    def readme_get(self):
        return wd(self.driver, self.timeout).until(EC.visibility_of_element_located(self.readme)).text
