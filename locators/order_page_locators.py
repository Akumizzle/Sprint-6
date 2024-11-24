from selenium.webdriver.common.by import By


name_field=[By.XPATH,".//input[@placeholder='* Имя']"]
surname_field=[By.XPATH,".//input[@placeholder='* Фамилия']"]
address_field=[By.XPATH,".//input[@placeholder='* Адрес: куда привезти заказ']"]
metro_field=[By.XPATH,".//input[@placeholder='* Станция метро']"]
phone_field=[By.XPATH,".//input[@placeholder='* Телефон: на него позвонит курьер']"]
date_field=[By.XPATH,".//input[@placeholder='* Когда привезти самокат']"]
period_field=[By.CSS_SELECTOR,".Dropdown-arrow"]#может нужен вейт?




period_1=[By.XPATH,".//div[text()='трое суток']"]
metro_station_1=[By.XPATH,".//li[@data-index='1']"]
next_button=[By.CSS_SELECTOR,'.Button_Middle__1CSJM']
order_button=[By.XPATH,".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
confirm_button=[By.XPATH,".//button[text()='Да']"]
check_status_button=[By.XPATH,".//button[text()='Посмотреть статус']"]
color_black=[By.XPATH,".//label[@for='black']"]
color_gray=[By.XPATH,".//label[@for='gray']"]
pop_up_window=[By.XPATH,".//div[@class='Order_Modal__YZ-d3']"]
logo_scooter=[By.CSS_SELECTOR,'.Header_LogoScooter__3lsAR']
logo_yandex=[By.CSS_SELECTOR,'.Header_LogoYandex__3TSOI']
pop_up_header=[By.CSS_SELECTOR,'.Order_ModalHeader__3FDaJ']



