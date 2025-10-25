from selenium.webdriver.common.by import By
class MainLocators:
    # Кнопка принять куки
    button_cookie = [By.XPATH, ".//button[@id='rcc-confirm-button']"]
    
    question_locator_list = [
        [By.XPATH, ".//div[@id='accordion__heading-0']"],
        [By.XPATH, ".//div[@id='accordion__heading-1']"],
        [By.XPATH, ".//div[@id='accordion__heading-2']"],
        [By.XPATH, ".//div[@id='accordion__heading-3']"],
        [By.XPATH, ".//div[@id='accordion__heading-4']"],
        [By.XPATH, ".//div[@id='accordion__heading-5']"],
        [By.XPATH, ".//div[@id='accordion__heading-6']"],
        [By.XPATH, ".//div[@id='accordion__heading-7']"]
    ]
    answer_locator_list = [
        [By.XPATH, ".//div[2][@aria-labelledby='accordion__heading-0']"],
        [By.XPATH, ".//div[2][@aria-labelledby='accordion__heading-1']"],
        [By.XPATH, ".//div[2][@aria-labelledby='accordion__heading-2']"],
        [By.XPATH, ".//div[2][@aria-labelledby='accordion__heading-3']"],
        [By.XPATH, ".//div[2][@aria-labelledby='accordion__heading-4']"],
        [By.XPATH,".//div[2][@aria-labelledby='accordion__heading-5']"],
        [By.XPATH,".//div[2][@aria-labelledby='accordion__heading-6']"],
        [By.XPATH,".//div[2][@aria-labelledby='accordion__heading-7']"]
    ]

    # Верхняя Кнопка Заказать
    button_order_top = [By.XPATH, ".//button[1][@class='Button_Button__ra12g']"]
    #Нижняя Кнопка Заказать
    button_order_down = [By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM')]"]

    # Логотип "Самокат"
    logo_scooter = [By.XPATH,".//img[@alt='Scooter']"]
    # Логотип "Яндекс"
    logo_yandex = [By.XPATH,".//img[@alt='Yandex']"]
    logo_dzen = [By.XPATH,".//*[@id='dzen-header']"]

