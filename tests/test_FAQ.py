from selenium import webdriver

import test_data
from conftest import driver
from locators import main_page_locators
from pages.main_page import MainPage
import test_url


class TestMainPageFAQ:

    def test_first_item_in_FAQ(self,driver):
        driver.get(test_url.main_page_url)
        main_page=MainPage(driver)
        main_page.scroll_to(main_page_locators.MainPageElements.first_question)
        main_page.click_button(main_page_locators.MainPageElements.first_question)
        text=main_page.get_element_text(main_page_locators.MainPageElements.first_answer)
        assert text==test_data.first_answer

    def test_second_item_in_FAQ(self,driver):
        driver.get(test_url.main_page_url)
        main_page=MainPage(driver)
        main_page.scroll_to(main_page_locators.MainPageElements.second_question)
        main_page.click_button(main_page_locators.MainPageElements.second_question)
        text = main_page.get_element_text(main_page_locators.MainPageElements.second_answer)
        assert text == test_data.second_answer

    def test_third_item_in_FAQ(self,driver):
        driver.get(test_url.main_page_url)
        main_page=MainPage(driver)
        main_page.scroll_to(main_page_locators.MainPageElements.third_question)
        main_page.click_button(main_page_locators.MainPageElements.third_question)
        text = main_page.get_element_text(main_page_locators.MainPageElements.third_answer)
        assert text == test_data.third_answer

    def test_fourth_item_in_FAQ(self,driver):
        driver.get(test_url.main_page_url)
        main_page=MainPage(driver)
        main_page.scroll_to(main_page_locators.MainPageElements.fourth_question)
        main_page.click_button(main_page_locators.MainPageElements.fourth_question)
        text = main_page.get_element_text(main_page_locators.MainPageElements.fourth_answer)
        assert text == test_data.fourth_answer

    def test_fifth_item_in_FAQ(self,driver):
        driver.get(test_url.main_page_url)
        main_page=MainPage(driver)
        main_page.scroll_to(main_page_locators.MainPageElements.fifth_question)
        main_page.click_button(main_page_locators.MainPageElements.fifth_question)
        text = main_page.get_element_text(main_page_locators.MainPageElements.fifth_answer)
        assert text == test_data.fifth_answer

    def test_sixth_item_in_FAQ(self,driver):
        driver.get(test_url.main_page_url)
        main_page=MainPage(driver)
        main_page.scroll_to(main_page_locators.MainPageElements.sixth_question)
        main_page.click_button(main_page_locators.MainPageElements.sixth_question)
        text = main_page.get_element_text(main_page_locators.MainPageElements.sixth_answer)
        assert text == test_data.sixth_answer

    def test_seventh_item_in_FAQ(self,driver):
        driver.get(test_url.main_page_url)
        main_page=MainPage(driver)
        main_page.scroll_to(main_page_locators.MainPageElements.seventh_question)
        main_page.click_button(main_page_locators.MainPageElements.seventh_question)
        text = main_page.get_element_text(main_page_locators.MainPageElements.seventh_answer)
        assert text == test_data.seventh_answer

    def test_eighth_item_in_FAQ(self,driver):
        driver.get(test_url.main_page_url)
        main_page=MainPage(driver)
        main_page.scroll_to(main_page_locators.MainPageElements.eighth_question)
        main_page.click_button(main_page_locators.MainPageElements.eighth_question)
        text = main_page.get_element_text(main_page_locators.MainPageElements.eighth_answer)
        assert text == test_data.eighth_answer
