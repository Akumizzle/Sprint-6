
from selenium.webdriver.common.by import By


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_field(self,field,filler):
        self.driver.find_element(*field).send_keys(filler)

    def click_button(self,button):
        self.driver.find_element(*button).click()

    def get_url(self):
        return self.driver.current_url

    def check_order_success(self):
        return 'Заказ оформлен' in self.driver.find_element(By.CSS_SELECTOR,'.Order_ModalHeader__3FDaJ').text


