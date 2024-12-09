from selenium.webdriver.common.by import By

class OrderPageElements:
    name_field=[By.XPATH,".//input[@placeholder='* Имя']"]
    surname_field=[By.XPATH,".//input[@placeholder='* Фамилия']"]
    address_field=[By.XPATH,".//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_field=[By.XPATH,".//input[@placeholder='* Станция метро']"]
    phone_field=[By.XPATH,".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    date_field=[By.XPATH,".//input[@placeholder='* Когда привезти самокат']"]
    period_field=[By.CSS_SELECTOR,".Dropdown-arrow"]

    period_1=[By.XPATH,".//div[text()='трое суток']"]
    metro_station_1=[By.XPATH,".//li[@data-index='1']"]
    next_button=[By.CSS_SELECTOR,"[class*='Button_Middle']"]
    order_button=[By.XPATH,".//button[contains(@class,'Button_Middle') and text()='Заказать']"]
    confirm_button=[By.XPATH,".//button[text()='Да']"]
    check_status_button=[By.XPATH,".//button[text()='Посмотреть статус']"]
    color_black=[By.XPATH,".//label[@for='black']"]
    color_gray=[By.XPATH,".//label[@for='gray']"]
    pop_up_window=[By.XPATH,".//div[contains(@class,'Order_Modal')]"]
    logo_scooter=[By.CSS_SELECTOR,"[class*='Header_LogoScooter']"]
    logo_yandex=[By.CSS_SELECTOR,"[class*='Header_LogoYandex']"]
    pop_up_header=[By.CSS_SELECTOR,"[class*='Order_ModalHeader']"]

    order_success_header=[By.CSS_SELECTOR,"[class*='Order_ModalHeader']"]



