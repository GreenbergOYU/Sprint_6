import allure
from locators.order_scooter_locators import OrderScooterLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    @allure.step('Заполняем поле Имя')
    def entry_input_name(self, user):
        self.insert_text(OrderScooterLocators.input_name, user.name)

    @allure.step('Заполняем поле Фамилия')
    def entry_input_surname(self, user):
        self.insert_text(OrderScooterLocators.input_surname, user.surname)

    @allure.step('Заполняем поле Адресс')
    def entry_input_adress(self, user):
        self.insert_text(OrderScooterLocators.input_adress, user.adress)

    @allure.step('Раскрываем список Метро')
    def click_list_metro(self):
        self.click_to_element(OrderScooterLocators.list_station_metro)

    @allure.step('Выбираем станцию Метро')
    def click_button_metro(self, user):
        metro_station_locator = (By.XPATH, f".//div[@class='select-search__select']//button[contains(., '{user.metro}')]")
        self.click_to_element(metro_station_locator)

    @allure.step('Заполняем поле телефон')
    def entry_input_phone_number(self, user):
        self.insert_text(OrderScooterLocators.input_phone_number, user.phone_number)

    @allure.step('Клик на кнопку "Далее"')
    def click_button_then(self):
        self.click_to_element(OrderScooterLocators.button_then)

    @allure.step('Клик на поле "Когда привезти самокат"')
    def click_calendar(self):
        self.click_to_element(OrderScooterLocators.input_when_bring_scooter)

    @allure.step('Выбор даты в календаре')
    def click_order_date(self, user):
        order_data = (By.XPATH, f".//*[@aria-label='{user.data}']")
        self.click_to_element(order_data)

    @allure.step('Клик на выпадающий список "Срок аренды"')
    def click_order_period(self):
        self.click_to_element(OrderScooterLocators.order_time)

    @allure.step('Выбор срока аренды')
    def choice_order_period(self, user):
        order_period_locator = (By.XPATH, f"//div[text()='{user.order_period}']")
        self.click_to_element(order_period_locator)

    @allure.step('Выбор цвета сомоката')
    def choice_color(self, user):
        color_locator = (By.XPATH, f".//*[text()='{user.color}']")
        self.click_to_element(color_locator)

    @allure.step('Заполняем поле комментарий')
    def entry_input_comment_courier(self, user):
        self.insert_text(OrderScooterLocators.input_comment_courier, user.comment_courier)

    @allure.step('Клик на кнопку "Заказать"')
    def click_button_order_confirm(self):
        self.click_to_element(OrderScooterLocators.button_order_confirm)       

    @allure.step('Подтверждение заказа в модальном окне "Хотите оформить заказ?"')
    def click_confirm_yes(self):
        self.click_to_element(OrderScooterLocators.confirm_yes)

    @allure.step('Проверка отображения модального окна  "Заказ оформлен"')
    def check_order_furnished(self):
        assert "Заказ оформлен" in  self.get_text_from_element(OrderScooterLocators.order_furnished)
         
