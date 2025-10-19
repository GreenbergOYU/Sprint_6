from selenium.webdriver.common.by import By
class Questions:
    # Кнопка принять куки
    button_cookie = [By.XPATH, ".//button[@id='rcc-confirm-button']"]
    # Клик на вопрос 1 "Сколько это стоит? И как оплатить?"
    question_price_payment = [By.XPATH, ".//div[@id='accordion__heading-0']"]
    # Ответ на вопрос 1 "Сколько это стоит? И как оплатить?"
    answer_price_payment = [By.XPATH, ".//div[2][@id='accordion__panel-0']"]
    # Клик на вопрос 2 "Хочу сразу несколько самокатов! Так можно?"
    question_several_scooters = [By.XPATH, ".//div[@id='accordion__heading-1']"]
    # Ответ на вопрос 2 "Хочу сразу несколько самокатов! Так можно?"
    answer_several_scooters = [By.XPATH, ".//div[2][@id='accordion__panel-1']"]
    # Клик на вопрос 3 "Как рассчитывается время аренды?"
    question_rental_time = [By.XPATH, ".//div[@id='accordion__heading-2']"]
    # Ответ на вопрос 3 "Как рассчитывается время аренды?"
    answer_rental_time = [By.XPATH, ".//div[2][@aria-labelledby='accordion__heading-2']"]
    # Клик на вопрос 4 "Можно ли заказать самокат прямо на сегодня?"
    question_order_scooter_today = [By.XPATH, ".//div[@id='accordion__heading-3']"]
    # Ответ на вопрос 4 "Можно ли заказать самокат прямо на сегодня?"
    answer_order_scooter_today = [By.XPATH, ".//div[2][@aria-labelledby='accordion__heading-3']"]
    # Клик на вопрос 5 "Можно ли продлить заказ или вернуть самокат раньше?"
    question_extend_return_scooter = [By.XPATH, ".//div[@id='accordion__heading-4']"]
    # Ответ на вопрос 5 "Можно ли продлить заказ или вернуть самокат раньше?"
    answer_extend_return_scooter = [By.XPATH, ".//div[2][@aria-labelledby='accordion__heading-4']"]
    # Клик на вопрос 6 "Вы привозите зарядку вместе с самокатом?"
    question_charging_scooter = [By.XPATH, ".//div[@id='accordion__heading-5']"]
    # Ответ на вопрос 6 "Вы привозите зарядку вместе с самокатом?"
    answer_charging_scooter = [By.XPATH,".//div[2][@aria-labelledby='accordion__heading-5']"]
    # Клик на вопрос 7 "Можно ли отменить заказ?"
    question_cancel_order = [By.XPATH, ".//div[@id='accordion__heading-6']"]
    # Ответ на вопрос 7 "Можно ли отменить заказ?"
    answer_cancel_order = [By.XPATH,".//div[2][@aria-labelledby='accordion__heading-6']"]
    # Клик на вопрос 8 "Я жизу за МКАДом, привезёте?"
    question_live_across_MKAD = [By.XPATH, ".//div[@id='accordion__heading-7']"]
    # Ответ на вопрос 8 "Я жизу за МКАДом, привезёте?"
    answer_live_across_MKAD = [By.XPATH,".//div[2][@aria-labelledby='accordion__heading-7']"]

class OrderURL:
    # Логотип "Самокат"
    logo_scooter = [By.XPATH,".//img[@alt='Scooter']"]
    # Логотип "Яндекс"
    logo_yandex = [By.XPATH,".//img[@alt='Yandex']"]
