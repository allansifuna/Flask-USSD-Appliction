from somo import db
from flask import current_app
from flask_login import UserMixin
from datetime import date
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .database import CRUDMixin
from random import sample


class Grade(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    question = db.relationship(
        'ExamQuestion', backref='gradequestion', cascade="all,delete", lazy=True)

    def __repr__(self):
        return f"{self.name}"


class Subject(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    question = db.relationship(
        'ExamQuestion', backref='subjectquestion', cascade="all,delete", lazy=True)

    def __repr__(self):
        return f"{self.name}"


class Student(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.String(40), nullable=False)
    question = db.relationship(
        'QuizSession', backref='quizstudent', cascade="all,delete", lazy=True)

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name} {self.phone_number})"

    @staticmethod
    def by_phoneNumber(phone_number):
        return Student.query.filter_by(phone_number=phone_number).first()

    @staticmethod
    def by_id(id):
        return Student.query.get(id)


# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))


class User(db.Model, UserMixin, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    role = db.Column(db.String(40), nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def get_reset_token(self, expires_sec=18000):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except Exception as e:
            return None
        return User.query.get(user_id)


class ExamQuestion(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    question = db.Column(db.String(100), nullable=False)
    option_A = db.Column(db.String(100), nullable=False)
    option_B = db.Column(db.String(100), nullable=False)
    option_C = db.Column(db.String(100), nullable=False)
    option_D = db.Column(db.String(100), nullable=False)
    answer = db.Column(db.String(10), nullable=False)
    explanation = db.Column(db.String(100), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'))
    session = db.relationship(
        'QuizSession', backref='quizsession', cascade="all,delete", lazy=True)
    def __repr__(self):
        return f"{self.question},{self.grade_id}"
    @staticmethod
    def select_questions(subject, grade):
        sub = Subject.query.filter_by(name=subject).first()
        grd = Grade.query.filter_by(name=f"Class {grade}").first()
        quest = ExamQuestion.query.filter_by(
            subject_id=sub.id, grade_id=grd.id).all()
        samples=sample(quest, 2)
        print(samples)
        return samples


class QuizSession(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('exam_question.id'))
    Student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    session_id = db.Column(db.String(200))
    complete = db.Column(db.Boolean, default=False)
    verdict = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"{id}-{self.question_id}-{self.Student_id}-{self.session_id}-{self.complete}-{self.verdict}"

    def update(self, verdict):
        self.complete = True
        self.verdict = verdict
        db.session.commit()

    @staticmethod
    def by_session(sess_id):
        print(QuizSession.query.all())
        quizs = QuizSession.query.filter_by(session_id=sess_id)

        return (quizs.filter_by(verdict=True).count(), quizs.count())


class AnonymousUser():
    pass
