from selenium.webdriver.common.by import By


class MainPage:


    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self,locator):
        element=self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_button(self,button):
        self.driver.find_element(*button).click()

    def get_parent_hidden_attribute(self,element):
        return self.driver.find_element(*element).find_element(By.XPATH, './..').get_attribute('hidden')






