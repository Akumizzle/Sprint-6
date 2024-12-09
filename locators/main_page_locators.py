from selenium.webdriver.common.by import By



class MainPageElements:

    first_question =[By.XPATH, ".//div[text()='Сколько это стоит? И как оплатить?']"]
    first_answer = [By.XPATH,".//div[@id='accordion__panel-0']/p"]

    second_question = [By.XPATH,".//div[text()='Хочу сразу несколько самокатов! Так можно?']"]
    second_answer = [By.XPATH,".//div[@id='accordion__panel-1']/p"]

    third_question = [By.XPATH,".//div[text()='Как рассчитывается время аренды?']"]
    third_answer = [By.XPATH,".//div[@id='accordion__panel-2']/p"]

    fourth_question = [By.XPATH,".//div[text()='Можно ли заказать самокат прямо на сегодня?']"]
    fourth_answer = [By.XPATH,".//div[@id='accordion__panel-3']/p"]

    fifth_question = [By.XPATH,".//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
    fifth_answer = [By.XPATH,".//div[@id='accordion__panel-4']/p"]

    sixth_question = [By.XPATH,".//div[text()='Вы привозите зарядку вместе с самокатом?']"]
    sixth_answer = [By.XPATH,".//div[@id='accordion__panel-5']/p"]

    seventh_question = [By.XPATH,".//div[text()='Можно ли отменить заказ?']"]
    seventh_answer = [By.XPATH,".//div[@id='accordion__panel-6']/p"]

    eighth_question = [By.XPATH,".//div[text()='Я жизу за МКАДом, привезёте?']"]
    eighth_answer = [By.XPATH,".//div[@id='accordion__panel-7']/p"]







