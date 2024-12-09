from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):




    def get_parent_hidden_attribute(self,element):
        return self.driver.find_element(*element).find_element(By.XPATH, './..').get_attribute('hidden')

    def get_element_text(self,element):
        return self.driver.find_element(*element).text





