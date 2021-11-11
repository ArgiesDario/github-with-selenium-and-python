import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserSetup:

    def __init__(self):
        options = Options()
        options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        current_path = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = current_path + r"\chromedriver.exe"
        self.driver = webdriver.Chrome(chromedriver_path, options=options)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.close()