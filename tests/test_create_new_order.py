from selenium import webdriver
from pages.main_page import MainPage
from locators import main_page_locators
from locators import order_page_locators
from pages.order_page import OrderPage
import test_data
import time
import pytest


class TestOrderCreate:

    driver=None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('name,surname,address,phone,date', [test_data.data_1,test_data.data_2])
    def test_new_order_top_button(self,name,surname,address,phone,date):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_button(main_page_locators.top_order_button)
        order_page=OrderPage(self.driver)
        order_page.fill_field(order_page_locators.name_field,name)
        order_page.fill_field(order_page_locators.surname_field,surname)
        order_page.fill_field(order_page_locators.address_field,address)
        order_page.click_button(order_page_locators.metro_field)
        order_page.click_button(order_page_locators.metro_station_1)
        order_page.fill_field(order_page_locators.phone_field,phone)
        order_page.click_button(order_page_locators.next_button)
        order_page.fill_field(order_page_locators.date_field,date)
        order_page.click_button(order_page_locators.period_field)
        order_page.click_button(order_page_locators.period_1)
        order_page.click_button(order_page_locators.color_black)
        order_page.click_button(order_page_locators.order_button)
        order_page.click_button(order_page_locators.confirm_button)
        assert order_page.check_order_success()
        order_page.click_button(order_page_locators.check_status_button)
        order_page.click_button(order_page_locators.logo_scooter)
        assert order_page.get_url()=='https://qa-scooter.praktikum-services.ru/'
        order_page.click_button(order_page_locators.logo_yandex)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert  order_page.get_url()=='https://dzen.ru/?yredirect=true'

    def test_new_order_bottom_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_button(main_page_locators.bottom_order_button)
        order_page=OrderPage(self.driver)
        order_page.fill_field(order_page_locators.name_field,test_data.name)
        order_page.fill_field(order_page_locators.surname_field,test_data.surname)
        order_page.fill_field(order_page_locators.address_field,test_data.address)
        order_page.click_button(order_page_locators.metro_field)
        order_page.click_button(order_page_locators.metro_station_1)
        order_page.fill_field(order_page_locators.phone_field,test_data.phone)
        order_page.click_button(order_page_locators.next_button)
        order_page.fill_field(order_page_locators.date_field,test_data.date)
        order_page.click_button(order_page_locators.period_field)
        order_page.click_button(order_page_locators.period_1)
        order_page.click_button(order_page_locators.color_black)
        order_page.click_button(order_page_locators.order_button)
        order_page.click_button(order_page_locators.confirm_button)
        assert order_page.check_order_success()
        order_page.click_button(order_page_locators.check_status_button)
        order_page.click_button(order_page_locators.logo_scooter)
        assert order_page.get_url()=='https://qa-scooter.praktikum-services.ru/'
        order_page.click_button(order_page_locators.logo_yandex)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert  order_page.get_url()=='https://dzen.ru/?yredirect=true'
