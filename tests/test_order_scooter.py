import allure
from locators.main_locators import MainLocators
from data import UserData1, UserData2
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderScooter:

    @pytest.mark.parametrize('button, user',
                             [
                              [MainLocators.button_order_top, UserData1],
                              [MainLocators.button_order_down, UserData2]
                              ],
                             )

    @allure.title('Заказ самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных.')
    def test_orderscooter(self, driver, button, user):
        self.main_page = MainPage(driver)
        self.order_page = OrderPage(driver)
        self.main_page.click_cookie()
        self.main_page.click_button_order(button)
        self.order_page.entry_input_name(user)
        self.order_page.entry_input_surname(user)
        self.order_page.entry_input_adress(user)
        self.order_page.click_list_metro()
        self.order_page.click_button_metro(user)
        self.order_page.entry_input_phone_number(user)
        self.order_page.click_button_then()
        self.order_page.click_calendar()
        self.order_page.click_order_date(user)
        self.order_page.click_order_period()
        self.order_page.choice_order_period(user)
        self.order_page.choice_color(user)
        self.order_page.entry_input_comment_courier(user)
        self.order_page.click_button_order_confirm()
        self.order_page.click_confirm_yes()
        self.order_page.check_order_furnished()