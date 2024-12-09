from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators import order_page_locators


class OrderPage(BasePage):


    def fill_field(self,field,filler):
        self.driver.find_element(*field).send_keys(filler)

    def check_order_success(self):
        return 'Заказ оформлен' in self.driver.find_element(*order_page_locators.OrderPageElements.order_success_header).text


