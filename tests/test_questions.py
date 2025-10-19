import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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

    def __init__(self, driver):
        self.driver = driver
    @allure.step('Скролл страницы вниз')
    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    @allure.step('Клик на кнопку принять куки')
    def click_cookie(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_cookie)).click()
    
    @allure.step('Клик на 1 вопрос "Сколько это стоит? И как оплатить?"')
    def click_question_price_payment(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.question_price_payment)).click()
    @allure.step('Ответ на 1 вопрос "Сутки — 400 рублей. Оплата курьеру — наличными или картой."')
    def check_question_price_payment(self):
        assert "Сутки — 400 рублей. Оплата курьеру — наличными или картой." in WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.answer_price_payment)).text

    @allure.step('Клик на 2 вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def click_question_several_scooters(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.question_several_scooters)).click()
    @allure.step('Ответ на 2 вопрос "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."')
    def check_question_several_scooters(self):
        assert "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим." in WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.answer_several_scooters)).text  
    
    @allure.step('Клик на вопрос 3 "Как рассчитывается время аренды?"')
    def click_question_rental_time(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.question_rental_time)).click()
    @allure.step('Ответ на 3 вопрос "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."')
    def check_question_rental_time(self):  
        assert "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30." in WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.answer_rental_time)).text
    
    
    @allure.step('Клик на вопрос 4 "Можно ли заказать самокат прямо на сегодня?"')
    def click_question_order_scooter_today(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.question_order_scooter_today)).click()
    @allure.step('Ответ на 4 вопрос "Только начиная с завтрашнего дня. Но скоро станем расторопнее."')
    def check_question_order_scooter_today(self):
        assert "Только начиная с завтрашнего дня. Но скоро станем расторопнее." in WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.answer_order_scooter_today)).text
    
    @allure.step('Клик на 5 вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def click_question_extend_return_scooter(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.question_extend_return_scooter)).click()
    @allure.step('Ответ на 5 вопрос "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."')
    def check_question_extend_return_scooter(self):
        assert "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010." in WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.answer_extend_return_scooter)).text
   
    @allure.step('Клик на 6 вопрос "Вы привозите зарядку вместе с самокатом?"')
    def click_question_charging_scooter(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.question_charging_scooter)).click()
    @allure.step('Ответ на 6 вопрос "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."')
    def check_question_charging_scooter(self):
        assert "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится." in WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.answer_charging_scooter)).text
    @allure.step('Клик на 7 вопрос "Можно ли отменить заказ?"')
    def click_question_cancel_order(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.question_cancel_order)).click()
    @allure.step('Ответ на 6 вопрос "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."')
    def check_question_cancel_order(self):
        assert "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои." in WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.answer_cancel_order)).text
    
    @allure.step('Клик на 8 вопрос "Я жизу за МКАДом, привезёте?"')
    def click_question_live_across_MKAD(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.question_live_across_MKAD)).click()
    @allure.step('Ответ на 8 вопрос "Да, обязательно. Всем самокатов! И Москве, и Московской области."')
    def check_question_live_across_MKAD(self):
        assert "Да, обязательно. Всем самокатов! И Москве, и Московской области." in WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.answer_live_across_MKAD)).text




class TestQuestions:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.Questions_page = Questions(cls.driver)
        cls.Questions_page.scroll_page()
        cls.Questions_page.click_cookie()

    @allure.title('Вопрос 1')
    @allure.description('Ответ на вопрос 1')

    def test_Questions1(self):
        self.Questions_page.click_question_price_payment()
        self.Questions_page.check_question_price_payment()
       

    @allure.title('Вопрос 2')
    @allure.description('Ответ на вопрос 2')    
    def test_Questions2(self):    
        self.Questions_page.click_question_several_scooters()
        self.Questions_page.check_question_several_scooters()
       
    @allure.title('Вопрос 3')
    @allure.description('Ответ на вопрос 3') 
    def test_Questions3(self):    
        self.Questions_page.click_question_rental_time()
        self.Questions_page.check_question_rental_time()
    
    @allure.title('Вопрос 4')
    @allure.description('Ответ на вопрос 4')     
    def test_Questions4(self):    
        self.Questions_page.click_question_order_scooter_today()
        self.Questions_page.check_question_order_scooter_today()
        
    @allure.title('Вопрос 5')
    @allure.description('Ответ на вопрос 5')    
    def test_Questions5(self):    
        self.Questions_page.click_question_extend_return_scooter()
        self.Questions_page.check_question_extend_return_scooter()
        
    @allure.title('Вопрос 6')
    @allure.description('Ответ на вопрос 6')     
    def test_Questions6(self):    
        self.Questions_page.click_question_charging_scooter()
        self.Questions_page.check_question_charging_scooter()
    
    @allure.title('Вопрос 7')
    @allure.description('Ответ на вопрос 7') 
    def test_Questions7(self):    
        self.Questions_page.click_question_cancel_order()
        self.Questions_page.check_question_cancel_order()
        
    @allure.title('Вопрос 8')
    @allure.description('Ответ на вопрос 8') 
    def test_Questions8(self):    
        self.Questions_page.click_question_live_across_MKAD()
        self.Questions_page.check_question_live_across_MKAD()
        

    @classmethod
    def teardown_class(cls):
        # закроем браузер
        cls.driver.quit()     




    