from selenium.webdriver.common.by import By
class OrderScooterLocators:
    # Кнопка принять куки
    button_cookie = [By.XPATH, ".//button[@id='rcc-confirm-button']"]
    # Кнопка "Заказать"
    button_order_top = [By.XPATH, ".//button[1][@class='Button_Button__ra12g']"]
    #
    button_order_down = [By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM')]"]
    # Поле "Имя"
    input_name = [By.XPATH, ".//input[@placeholder='* Имя']"]
    # Поле "Фамилия"
    input_surname = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    # Поле "Адрес"
    input_adress = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    # Выпадающий список "Станция метро"
    list_station_metro = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    # Поле "Телефон"
    input_phone_number = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    # Кнопка "Далее"
    button_then = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    # Поле "Когда привезти самокат"
    input_when_bring_scooter = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    # Выбор даты в календаре
    order_date = [By.XPATH,".//div[6][@aria-label='Choose суббота, 25-е октября 2025 г.']"]
    # Выпадающий список "Срок аренды"
    order_time = [By.XPATH,".//div[@class='Dropdown-control']"]
    # Выбор значения из выпадающего списка "Срок аренды" - "трое суток"
    order_time_three_days = [By.XPATH,".//*[text()='двое суток']"]
    # Активация чек бокса "серая безысходность"
    check_box_gray = [By.XPATH, ".//*[text()='серая безысходность']"]
    # Поле "Комментарий для курьера"
    input_comment_courier = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    # Кнопка подтверждение заказа "Заказать"
    button_order_confirm = [By.XPATH, ".//button[2][@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    # Модальное окно "Хотите оформить заказ?"
    modal_window = [By.XPATH, ".//div[5][@class='Order_Modal__YZ-d3']"]
    # Подтверждение заказа в модальном окне "Хотите оформить заказ?"
    confirm_yes =  [By.XPATH,".//*[text()='Да']"]
    # Модальное окно "Заказ оформлен"
    order_furnished = [By.XPATH,".//*[text()='Заказ оформлен']"]
    # Кнопка "Посмотреть статус"
    button_view_status = [By.XPATH,".//*[text()='Посмотреть статус']"]
    # Логотип "Самокат"
    logo_scooter = [By.XPATH,".//img[@alt='Scooter']"]
    # Логотип "Яндекс"
    logo_yandex = [By.XPATH,".//img[@alt='Yandex']"]
