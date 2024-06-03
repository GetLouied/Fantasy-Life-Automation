from selenium.webdriver.common.by import By
from base_page import BasePage

class HomePage(BasePage):
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".far.fa-search")
    LOGIN_BUTTON = (By.XPATH, "//a[@class='btn btn-outline-light']")
    SUBSCRIBE_EMAIL_INPUT = (By.CSS_SELECTOR, "div[class='px-3 mb-3'] input[placeholder='youremail@here.com']")
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-secondary w-100 fl-font-size-15 fl-font-weight-700 fl-font-space text-uppercase']")
    SUBSCRIBE_CONFIRMATION = (By.XPATH, "//div[@class='text-success']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.fantasylife.com/")

    def click_search(self):
        search_button = self.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def click_to_login_page(self):
        login_button = self.find_element(*self.LOGIN_BUTTON)
        login_button.click()
    
    def subscribe_to_newsletter(self, email):
        email_input = self.find_element(*self.SUBSCRIBE_EMAIL_INPUT)
        email_input.send_keys(email)
        subscribe_button = self.find_element(*self.SUBSCRIBE_BUTTON)
        subscribe_button.click()

    def get_confirmation_message(self):
        return self.find_element(*self.SUBSCRIBE_CONFIRMATION).text
    

    # Quick test to make sure the above works, will be moved to a seperate test file
if __name__ == "__main__":

    driver = BasePage.create_chrome_driver()

    home_page = HomePage(driver)
    home_page.click_search()
    driver.navigate().back()
    home_page.click_to_login_page()
    driver.navigate().back()
    home_page.subscribe_to_newsletter("derienzo_louis@yahoo.com")
    confirmation_message = home_page.get_confirmation_message()
    print("Confirmation message:", confirmation_message)

    driver.quit()