from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

import time

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
        email_input.clear()
        email_input.send_keys(email)
        subscribe_button = self.find_element(*self.SUBSCRIBE_BUTTON)
        subscribe_button.click()
        time.sleep(2)

    def get_confirmation_message(self):
        return self.find_element(*self.SUBSCRIBE_CONFIRMATION).text
        
    def check_for_validation_error(self):
        email_input = self.find_element(*self.SUBSCRIBE_EMAIL_INPUT)
        return email_input.get_attribute("validationMessage")
    
    def check_responsive_design(self, widths):
        for width in widths:
            self.driver.set_window_size(width, 800)
            self.driver.refresh()
            
            try:
                assert self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > nav:nth-child(1) > div:nth-child(3)").is_displayed(), f"Navigation not displayed at width {width}"
                print(f"Responsive design check passed for width: {width}")
            except AssertionError as e:
                print(f"Responsive design check failed for width {width}: {e}")

    def hover_and_click_dropdown_nav_links(self, nav_locator):
        actions = ActionChains(self.driver)

        def locate_nav_and_links():
            nav_bar = self.find_element(*nav_locator)
            actions.move_to_element(nav_bar).perform()
            time.sleep(2)  
            dropdown_links = nav_bar.find_elements(By.TAG_NAME, 'a')
            return nav_bar, dropdown_links

        nav_bar, dropdown_links = locate_nav_and_links()

        for i in range(1, len(dropdown_links)):
            try:
                nav_bar, dropdown_links = locate_nav_and_links()  
                link = dropdown_links[i]
                actions.move_to_element(link).click().perform()
                self.driver.back()
                time.sleep(2)
            except (StaleElementReferenceException, NoSuchElementException, IndexError) as e:
                nav_bar, dropdown_links = locate_nav_and_links()

    

    # Quick example tests to make sure the above works, will be moved to a proper test file

# if __name__ == "__main__":

#     driver = BasePage.create_chrome_driver()
#     invalid_email = "123hhh"
#     valid_email = "derienzo_louis@yahoo.com"

#     home_page = HomePage(driver)
#     # home_page.click_search()
#     # driver.back()
#     # home_page.click_to_login_page()
#     # driver.back()
#     # time.sleep(5)

#     # home_page.subscribe_to_newsletter(invalid_email)
#     # validation_error = home_page.check_for_validation_error()
#     # if validation_error:
#     #     print(f"Validation failed as expected for invalid email: {validation_error}")
#     # else:
#     #     print("Expected validation error for invalid email was not found.")
#     # time.sleep(5)
    
#     # home_page.subscribe_to_newsletter(valid_email)
#     # confirmation_message = home_page.get_confirmation_message()
#     # print("Confirmation message:", confirmation_message)

#     # time.sleep(2)

#     # home_page.check_responsive_design([1200, 992, 768, 576])

#     # Tip: Use Parent_element.find_elements by Tag_name

#     nav_locator = (By.CSS_SELECTOR, "body > div:nth-child(2) > header:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > nav:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(1)")
#     home_page.hover_and_click_dropdown_nav_links(nav_locator)

#     driver.quit()