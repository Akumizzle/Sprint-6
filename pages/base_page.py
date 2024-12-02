
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self,locator):
        element=self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_button(self,button):
        self.driver.find_element(*button).click()

    def get_url(self):
        return self.driver.current_url
