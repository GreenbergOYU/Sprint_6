import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators.order_scooter_locators import OrderScooterLocators
from selenium.common.exceptions import NoSuchElementException
from user_data import UserData1, UserData2
import pytest

import time
# Тест кейс заказ самоката##
class OrderScooterActions:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик на кнопку принять куки')
    def click_cookie(self):
        try:
            self.driver.find_element(*OrderScooterLocators.button_cookie).click()
        except NoSuchElementException:
            pass
    
    @allure.step('Клик на кнопку "Заказать"')
    def click_button_order(self, button):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button)).click()
    
    @allure.step('Заполнение поля "Имя"')
    def entry_input_name(self,user):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.input_name)).send_keys(user.name)
    @allure.step('Заполнение поля "Фамилия"')
    def entry_input_surname(self,user):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.input_surname)).send_keys(user.surname)
    @allure.step('Заполнение поля "Адрес"')
    def entry_input_adress(self,user):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.input_adress)).send_keys(user.adress)
    @allure.step('Клик на выпадающий список "Станция метро" и выбор станции метро')
    def click_list_station_metro(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.list_station_metro)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.list_station_metro)).send_keys(Keys.DOWN)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.list_station_metro)).send_keys(Keys.RETURN)
    @allure.step('Заполнение поля "Телефон"')
    def entry_input_phone_number(self,user):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.input_phone_number)).send_keys(user.phone_number)
    @allure.step('Клик на кнопку "Далее"')
    def click_button_then(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.button_then)).click()
    @allure.step('Клик на поле "Когда привезти самокат"')
    def click_input_when_bring_scooter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.input_when_bring_scooter)).click()
    @allure.step('Выбор даты в календаре')
    def click_order_date(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.order_date)).click()
    @allure.step('Клик на выпадающий список "Срок аренды"')
    def click_order_time(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.order_time)).click()
    @allure.step('Выбираем срок аренды из списка "Срок аренды" - 3 суток')
    def choice_order_time_three_days(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.order_time_three_days)).click()
    @allure.step('Выбираем цвет самоката "серая безысходность"')
    def choice_color_scooter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.check_box_gray)).click()
    @allure.step('Заполнение поля "Комментарий для курьера"')
    def entry_input_comment_courier(self,user):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.input_comment_courier)).send_keys(user.comment_courier)
    @allure.step('Клик на кнопку "Заказать"')
    def click_button_order_confirm(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.button_order_confirm)).click()
    @allure.step('Подтверждение заказа в модальном окне "Хотите оформить заказ?"')
    def click_confirm_yes(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.confirm_yes)).click()
    @allure.step('Проверка отображения модального окна  "Заказ оформлен"')
    def check_order_furnished(self):
        assert "Заказ оформлен" in WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.order_furnished)).text
    @allure.step('Клик на кнопку "Посмотреть статус"')
    def click_button_view_status(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.button_view_status)).click()
    @allure.step('Клик на логотип "Самокат"')
    def click_logo_scooter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderScooterLocators.logo_scooter)).click()
    @allure.step('Проверка ссылки ')
    def check_URL(self):
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/" 





class TestOrderScooter:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.OrderScooter_page = OrderScooterActions(cls.driver)

    @pytest.mark.parametrize('button, user',
                             [
                              [OrderScooterLocators.button_order_top, UserData1],
                              [OrderScooterLocators.button_order_down, UserData2]
                              ],
                             )

    @allure.title('Заказ самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных.')
    def test_OrderScooter(self, button, user):
        self.OrderScooter_page.click_cookie()
        self.OrderScooter_page.click_button_order(button)
        self.OrderScooter_page.entry_input_name(user)
        self.OrderScooter_page.entry_input_surname(user)
        self.OrderScooter_page.entry_input_adress(user)
        self.OrderScooter_page.click_list_station_metro()
        
        
        self.OrderScooter_page.entry_input_phone_number(user)
        
        self.OrderScooter_page.click_button_then()
        
        self.OrderScooter_page.click_input_when_bring_scooter()
         
        self.OrderScooter_page.click_order_date()
         
        self.OrderScooter_page.click_order_time()
        
        self.OrderScooter_page.choice_order_time_three_days()
        
        self.OrderScooter_page.choice_color_scooter()
        
        self.OrderScooter_page.entry_input_comment_courier(user)
        
        self.OrderScooter_page.click_button_order_confirm()
        
        self.OrderScooter_page.click_confirm_yes()
        
        self.OrderScooter_page.check_order_furnished()
        
        self.OrderScooter_page.click_button_view_status()
        
        self.OrderScooter_page.click_logo_scooter()
        
        self.OrderScooter_page.check_URL()
        
    @classmethod
    def teardown_class(cls):
        # закроем браузер
        cls.driver.quit()     
    