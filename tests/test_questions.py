import allure
import pytest
from pages.main_page import MainPage
from data import CorrectAnswer


class TestQuestions:
    @allure.title('Проверяем выпадающий список вопросы-ответы')
    @pytest.mark.parametrize("index", [0,1,2,3,4,5,6,7])
    def test_questions(self, driver, index):
        self.main_page = MainPage(driver)
        # Прокрутка до конца страницы
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        self.main_page.click_to_question(index)
        actual_answer = self.main_page.get_answer_text(index)
        assert actual_answer == CorrectAnswer.correct_answer_list[index]
