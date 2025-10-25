import allure
from selenium.common.exceptions import NoSuchElementException
from locators.main_locators import MainLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Клик на кнопку принять куки')
    def click_cookie(self):
        try:
            return self.click_to_element(MainLocators.button_cookie)
        except NoSuchElementException:
            pass

    @allure.step('Клик на Вопрос')
    def click_to_question (self, index):
        self.click_to_element(MainLocators.question_locator_list[index])

    @allure.step('Получение ответа на Вопрос')
    def get_answer_text(self, index):
        return self.get_text_from_element(MainLocators.answer_locator_list[index])
    
    @allure.step('Клик на кнопку "Заказать"')
    def click_button_order(self, button):
        self.click_to_element(button)

    @allure.step('Клик на логотип "Сатокат"')
    def click_logo_scooter(self):
        self.click_to_element(MainLocators.logo_scooter)
    
    @allure.step('Клик на логотип "Яндекс"')
    def click_logo_yandex(self):
        self.click_to_element(MainLocators.logo_yandex)

    @allure.step('Ожидаем загрузки страницы "Яндекс"')
    def wait_yandex(self):
        self.get_text_from_element(MainLocators.logo_dzen)

        