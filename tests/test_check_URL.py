import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Тест кейс клик  на логотип «Самоката», клик на логотип "Яндекс"##
class OrderURL:
    # Логотип "Самокат"
    logo_scooter = [By.XPATH,".//img[@alt='Scooter']"]
    # Логотип "Яндекс"
    logo_yandex = [By.XPATH,".//img[@alt='Yandex']"]

    logo_dzen = [By.XPATH,".//*[@id='dzen-header']"]


    

    def __init__(self, driver):
        self.driver = driver
    @allure.step('Клик на логотип "Самокат"')
    def click_logo_scooter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.logo_scooter)).click()
    @allure.step('Проверка ссылки "Самокат"')
    def check_URL_scooter(self):
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"
    @allure.step('Клик на логотип "Яндекс"')
    def click_logo_yandex(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.logo_yandex)).click()
    def switch_win(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    @allure.step('Ожидание загрузки страницы Дзен')
    def wait_yandex(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.logo_dzen))

    @allure.step('Проверка ссылки "Яндекс"')
    def check_URL_yandex(self):
        assert self.driver.current_url == "https://dzen.ru/?yredirect=true"

class TestOrderURLScooter:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.OrderURLScooter_page = OrderURL(cls.driver)
    
    @allure.title('Клик на логотип "Самокат"')
    @allure.description('Проверяем, что попадаем  на главную страницу «Самоката».')
    def test_OrderURL(self):
        self.OrderURLScooter_page.click_logo_scooter()
        
        self.OrderURLScooter_page.check_URL_scooter()
        
    @classmethod
    def teardown_class(cls):
        # закроем браузер
        cls.driver.quit()

class TestOrderURLYandex:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.OrderURLYandex_page = OrderURL(cls.driver)
    
    @allure.title('Клик на логотип "Яндекс"')
    @allure.description('Проверяем, что в новом окне через редирект откроется главная страница Дзена.')
    def test_OrderURL(self):
        self.OrderURLYandex_page.click_logo_yandex()

        self.OrderURLYandex_page.switch_win()

        self.OrderURLYandex_page.wait_yandex()

        self.OrderURLYandex_page.check_URL_yandex()
        

    @classmethod
    def teardown_class(cls):
        # закроем браузер
        cls.driver.quit()