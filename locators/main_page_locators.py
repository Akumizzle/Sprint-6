from selenium.webdriver.common.by import By



class MainPageElements:

    first_question =[By.XPATH, ".//div[text()='Сколько это стоит? И как оплатить?']"]
    first_answer = [By.XPATH,".//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"]

    second_question = [By.XPATH,".//div[text()='Хочу сразу несколько самокатов! Так можно?']"]
    second_answer = [By.XPATH,".//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']"]

    third_question = [By.XPATH,".//div[text()='Как рассчитывается время аренды?']"]
    third_answer = [By.XPATH,".//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']"]

    fourth_question = [By.XPATH,".//div[text()='Можно ли заказать самокат прямо на сегодня?']"]
    fourth_answer = [By.XPATH,".//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"]

    fifth_question = [By.XPATH,".//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
    fifth_answer = [By.XPATH,".//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']"]

    sixth_question = [By.XPATH,".//div[text()='Вы привозите зарядку вместе с самокатом?']"]
    sixth_answer = [By.XPATH,".//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"]

    seventh_question = [By.XPATH,".//div[text()='Можно ли отменить заказ?']"]
    seventh_answer = [By.XPATH,".//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"]

    eighth_question = [By.XPATH,".//div[text()='Я жизу за МКАДом, привезёте?']"]
    eighth_answer = [By.XPATH,".//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']"]

    top_order_button=[By.XPATH,".//button[text()='Заказать']"]
    bottom_order_button = [By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div[5]/button"]# ищет кнопку только так
    #bottom_order_button=[By.CSS_SELECTOR,"[class*='Button_UltraBig')]"]                  # испробовал 2 варианта ниже
    #bottom_order_button = [By.XPATH, ".//button[contains(@class,'Button_UltraBig')]"]

    logo_scooter = [By.CSS_SELECTOR, "[class*='Header_LogoScooter']"]
    logo_yandex = [By.CSS_SELECTOR, "[class*='Header_LogoYandex']"]



