from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import Chrome, Firefox, Edge, Safari
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def find_element(self, *locator):
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not found within timelimit')
            return None

    def find_elements(self, *locator):
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            print(f'Elements with locator {locator} not found within timelimit')
            return []
    
    @staticmethod
    def create_chrome_driver(headless=False, incognito=False, disable_notifications=False, page_load_strategy='normal'):
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        if headless: 
            chrome_options.add_argument("--headless")
        if incognito:
            chrome_options.add_argument("--incognito")
        if disable_notifications:
            chrome_options.add_argument("--disable-notifications")
        chrome_options.page_load_strategy = page_load_strategy

        driver = Chrome(options=chrome_options)
        return driver
    
    @staticmethod
    def create_firefox_driver(headless=False, private=False, page_load_strategy='normal'):
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument("-headless")
        if private:
            firefox_options.add_argument("-private")
        firefox_options.page_load_strategy = page_load_strategy
        
        driver = Firefox(options=firefox_options)
        return driver
    
    @staticmethod
    def create_edge_driver(headless=False, incognito=False, page_load_strategy='normal'):
        edge_options = EdgeOptions()
        if headless: 
            edge_options.add_argument("--headless")
        if incognito:
            edge_options.add_argument("--inprivate")
        edge_options.page_load_strategy = page_load_strategy

        driver = Edge(options=edge_options)
        return driver
    
    @staticmethod
    def create_safari_driver():

        driver = Safari()
        return driver
    
    @staticmethod
    def quit_driver(driver):
        driver.quit()