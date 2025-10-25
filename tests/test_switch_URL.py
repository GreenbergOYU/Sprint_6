import allure
from pages.main_page import MainPage
from data import UrlData



class TestOrderURLScooter:
    @allure.title('Клик на логотип "Самокат"')
    @allure.description('Проверяем, что попадаем  на главную страницу «Самоката».')
    def test_switch_url_scooter(self, driver):
        self.main_page = MainPage(driver)
        self.main_page.click_logo_scooter()
        assert UrlData.URL == self.main_page.check_URL()

    @allure.title('Клик на логотип "Яндекс"')
    @allure.description('Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_switch_url_yandex(self, driver):
        self.main_page = MainPage(driver)
        self.main_page.click_logo_yandex()
        self.main_page.switch_win()
        self.main_page.wait_yandex()
        assert UrlData.url_dzen == self.main_page.check_URL()

        

 