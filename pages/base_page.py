
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # кликает по элементу
    @allure.title('Кликаем по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()

    # получает текст элемента
    @allure.title('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).text
    
    @allure.title('Ввод текста')
    def insert_text(self, locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.title('Получаем урл текущей вкладки')
    def check_URL(self):
        return self.driver.current_url

    @allure.title('Переходим на последнюю вкладку')
    def switch_win(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  


