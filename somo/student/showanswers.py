# query 10 questions according to class and subject
# save the questions in the database
# query them one by one while asking the user while saving the id in the session
# while updating the complete
from ..base_menu import Menu
from .utils import subjects
from ..models import ExamQuestion, QuizSession, Student
from somo import db


class ShowAnswersMenu(Menu):
    def show_answers(self):
        res = int(self.user_response)
        if res == 0:
            return self.home()
        if self.session.get('wrong_questions') == []:
            menu_text = "You have no more questions left.\n"\
                "0. Take a new quiz"
            return sef.ussd_proceed(menu_text)
        return self.display_answers()

    def display_answers(self):
        ids = self.session.get('wrong_questions').pop(0)
        quiz = ExamQuestion.query.get(ids)
        ans = quiz.answer
        if ans == "A":
            v = quiz.option_A
        elif ans == "B":
            v = quiz.option_B
        elif ans == "C":
            v = quiz.option_C
        else:
            v = quiz.option_D
        menu_text = f"{quiz.question}:-\n"\
            f"A. {quiz.option_A}\n"\
            f"B. {quiz.option_B}\n"\
            f"C. {quiz.option_C}\n"\
            f"D. {quiz.option_D}\n\n"\
            f"Answer: {ans}. {v}.\n\n"\
            f"{quiz.explanation}.\n\n"
        if self.session.get('wrong_questions') != []:
            menu_text += f"1. Next question.\n"
        menu_text += f"0. Take a new quiz."
        return self.ussd_proceed(menu_text)

    def execute(self):

        menu = {
            5: self.show_answers,
        }
        return menu.get(self.level)()
