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
        main_page.click_button(main_page_locators.MainPageElements.top_order_button)
        order_page=OrderPage(self.driver)
        order_page.fill_field(order_page_locators.OrderPageElements.name_field,name)
        order_page.fill_field(order_page_locators.OrderPageElements.surname_field,surname)
        order_page.fill_field(order_page_locators.OrderPageElements.address_field,address)
        order_page.click_button(order_page_locators.OrderPageElements.metro_field)
        order_page.click_button(order_page_locators.OrderPageElements.metro_station_1)
        order_page.fill_field(order_page_locators.OrderPageElements.phone_field,phone)
        order_page.click_button(order_page_locators.OrderPageElements.next_button)
        order_page.fill_field(order_page_locators.OrderPageElements.date_field,date)
        order_page.click_button(order_page_locators.OrderPageElements.period_field)
        order_page.click_button(order_page_locators.OrderPageElements.period_1)
        order_page.click_button(order_page_locators.OrderPageElements.color_black)
        order_page.click_button(order_page_locators.OrderPageElements.order_button)
        order_page.click_button(order_page_locators.OrderPageElements.confirm_button)
        assert order_page.check_order_success()

    def test_new_order_bottom_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.scroll_to(main_page_locators.MainPageElements.bottom_order_button)
        main_page.click_button(main_page_locators.MainPageElements.bottom_order_button)
        order_page=OrderPage(self.driver)
        order_page.fill_field(order_page_locators.OrderPageElements.name_field,test_data.name)
        order_page.fill_field(order_page_locators.OrderPageElements.surname_field,test_data.surname)
        order_page.fill_field(order_page_locators.OrderPageElements.address_field,test_data.address)
        order_page.click_button(order_page_locators.OrderPageElements.metro_field)
        order_page.click_button(order_page_locators.OrderPageElements.metro_station_1)
        order_page.fill_field(order_page_locators.OrderPageElements.phone_field,test_data.phone)
        order_page.click_button(order_page_locators.OrderPageElements.next_button)
        order_page.fill_field(order_page_locators.OrderPageElements.date_field,test_data.date)
        order_page.click_button(order_page_locators.OrderPageElements.period_field)
        order_page.click_button(order_page_locators.OrderPageElements.period_1)
        order_page.click_button(order_page_locators.OrderPageElements.color_black)
        order_page.click_button(order_page_locators.OrderPageElements.order_button)
        order_page.click_button(order_page_locators.OrderPageElements.confirm_button)
        assert order_page.check_order_success()

    def test_logo_yandex_redirect(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_button(main_page_locators.MainPageElements.logo_yandex)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert main_page.get_url() == 'https://dzen.ru/?yredirect=true'

    def test_logo_scooter_redirect(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_button(main_page_locators.MainPageElements.top_order_button)
        main_page.click_button(order_page_locators.OrderPageElements.logo_scooter)
        assert main_page.get_url() == 'https://qa-scooter.praktikum-services.ru/'