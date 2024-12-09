from selenium.webdriver.common.by import By



class BasePageElements:


    top_order_button = [By.XPATH, ".//button[text()='Заказать']"]
    bottom_order_button = [By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div[5]/button"]  # ищет кнопку только так
    # bottom_order_button=[By.CSS_SELECTOR,"[class*='Button_UltraBig')]"]                  # испробовал 2 варианта ниже
    # bottom_order_button = [By.XPATH, ".//button[contains(@class,'Button_UltraBig')]"]

    logo_scooter = [By.CSS_SELECTOR, "[class*='Header_LogoScooter']"]
    logo_yandex = [By.CSS_SELECTOR, "[class*='Header_LogoYandex']"]


