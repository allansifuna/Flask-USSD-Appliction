# query 10 questions according to class and subject
# save the questions in the database
# query them one by one while asking the user while saving the id in the session
# while updating the complete
from ..base_menu import Menu
from .utils import subjects
from ..models import ExamQuestion, QuizSession, Student
from somo import db


class AnswerQuestionsMenu(Menu):
    def query_questions(self):
        res = int(self.user_response)
        if res == 2 or res == 0:
            return self.home()
        s = ExamQuestion.select_questions(
            self.session['subject'], self.session['grade'])
        std = self.user
        for i in s:
            v = QuizSession(quizsession=i, quizstudent=std,
                            session_id=self.session['session_id'])
            v.save()
            # print("v:", v)
            self.session['questions'].append(i.id)
        self.session['level'] = 40
        return self.display_question()

    def display_question(self):
        ids = self.session.get('questions').pop(0)
        quiz_sess = QuizSession.query.filter_by(
            question_id=ids, session_id=self.session['session_id']).first()
        # print(f"cv: q_id {ids},s_id {self.session['session_id']},all {QuizSession.query.all()}")
        self.session['questions_done'].append(quiz_sess.id)
        quiz = ExamQuestion.query.get(ids)
        menu_text = f"{quiz.question}:-\n"\
            f"A. {quiz.option_A}\n"\
            f"B. {quiz.option_B}\n"\
            f"C. {quiz.option_C}\n"\
            f"D. {quiz.option_D}\n"
        return self.ussd_proceed(menu_text)

    def answer_question(self):  # 50
        answer = self.user_response
        quiz = QuizSession.query.get(self.session.get('questions_done')[-1])
        quest = ExamQuestion.query.get(quiz.question_id)
        quiz.update(quest.answer == answer.upper())
        if not quest.answer == answer.upper():
            self.session['wrong_questions'].append(quest.id)
        ses = quiz.session_id

        if self.session.get('questions') == []:
            s = QuizSession.by_session(ses)
            if s[0] == s[1]:
                menu_text = f"Congratulations!! You have gotten {s[0]} questions right out of {s[1]}.\n"\
                    "0. Take another test.\n"
                self.session['level'] = 4
                return self.ussd_proceed(menu_text)
            else:
                menu_text = f"You have gotten {s[0]} questions right out of {s[1]}.\n"\
                    f"1. View answers to failed questions.\n"\
                    f"0. Back.\n"
                self.session['level'] = 5
                return self.ussd_proceed(menu_text)
        else:
            return self.display_question()

    def execute(self):

        menu = {
            4: self.query_questions,
            40: self.answer_question
        }
        return menu.get(self.level)()
