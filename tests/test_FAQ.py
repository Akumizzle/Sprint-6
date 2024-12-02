from selenium import webdriver

from locators import main_page_locators
from pages.main_page import MainPage


class TestMainPageFAQ:

    driver=None

    @classmethod
    def setup_class(cls):
        cls.driver=webdriver.Chrome()

    def test_first_item_in_FAQ(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page=MainPage(self.driver)
        main_page.scroll_to(main_page_locators.MainPageElements.first_question)
        main_page.click_button(main_page_locators.MainPageElements.first_question)
        attribute=main_page.get_parent_hidden_attribute(main_page_locators.MainPageElements.first_answer)
        assert attribute is None

    def test_second_item_in_FAQ(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page=MainPage(self.driver)
        main_page.scroll_to(main_page_locators.MainPageElements.second_question)
        main_page.click_button(main_page_locators.MainPageElements.second_question)
        attribute=main_page.get_parent_hidden_attribute(main_page_locators.MainPageElements.second_answer)
        assert attribute is None

    def test_third_item_in_FAQ(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page=MainPage(self.driver)
        main_page.scroll_to(main_page_locators.MainPageElements.third_question)
        main_page.click_button(main_page_locators.MainPageElements.third_question)
        attribute=main_page.get_parent_hidden_attribute(main_page_locators.MainPageElements.third_answer)
        assert attribute is None

    def test_fourth_item_in_FAQ(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page=MainPage(self.driver)
        main_page.scroll_to(main_page_locators.MainPageElements.fourth_question)
        main_page.click_button(main_page_locators.MainPageElements.fourth_question)
        attribute=main_page.get_parent_hidden_attribute(main_page_locators.MainPageElements.fourth_answer)
        assert attribute is None

    def test_fifth_item_in_FAQ(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page=MainPage(self.driver)
        main_page.scroll_to(main_page_locators.MainPageElements.fifth_question)
        main_page.click_button(main_page_locators.MainPageElements.fifth_question)
        attribute=main_page.get_parent_hidden_attribute(main_page_locators.MainPageElements.fifth_answer)
        assert attribute is None

    def test_sixth_item_in_FAQ(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page=MainPage(self.driver)
        main_page.scroll_to(main_page_locators.MainPageElements.sixth_question)
        main_page.click_button(main_page_locators.MainPageElements.sixth_question)
        attribute=main_page.get_parent_hidden_attribute(main_page_locators.MainPageElements.sixth_answer)
        assert attribute is None

    def test_seventh_item_in_FAQ(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page=MainPage(self.driver)
        main_page.scroll_to(main_page_locators.MainPageElements.seventh_question)
        main_page.click_button(main_page_locators.MainPageElements.seventh_question)
        attribute=main_page.get_parent_hidden_attribute(main_page_locators.MainPageElements.seventh_answer)
        assert attribute is None

    def test_eighth_item_in_FAQ(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page=MainPage(self.driver)
        main_page.scroll_to(main_page_locators.MainPageElements.eighth_question)
        main_page.click_button(main_page_locators.MainPageElements.eighth_question)
        attribute=main_page.get_parent_hidden_attribute(main_page_locators.MainPageElements.eighth_answer)
        assert attribute is None

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()