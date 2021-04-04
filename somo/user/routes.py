from flask import Blueprint, render_template, redirect, url_for, send_from_directory, current_app
from somo.models import ExamQuestion, Grade, Subject
from somo.user.forms import AddSubject, AddGrade, AddQuestion
import os
import json

user = Blueprint('user', __name__)


def getgrade():
    return Grade.query.all()


def get_grade_pk(obj):
    return str(obj)


def getsubject():
    return Subject.query.all()


def get_subject_pk(obj):
    return str(obj)


@user.route('/')
def home():
    return render_template('index.html')


@user.route('/add-question', methods=['GET', 'POST'])
def add_question():
    form = AddQuestion()
    form.grade.get_pk = get_grade_pk
    form.grade.query_factory = getgrade
    form.subject.get_pk = get_subject_pk
    form.subject.query_factory = getsubject
    if form.validate_on_submit():
        quiz = ExamQuestion(question=form.question.data, option_A=form.option_A.data, option_B=form.option_B.data,
                            option_C=form.option_C.data, option_D=form.option_D.data, explanation=form.explanation.data,
                            answer=form.answer.data, subjectquestion=form.subject.data, gradequestion=form.grade.data)
        quiz.save()
        # return redirect(url_for('user.home'))
    form.question.data = ""
    form.option_A.data = ""
    form.option_B.data = ""
    form.option_C.data = ""
    form.option_D.data = ""
    form.explanation.data = ""
    form.answer.data = ""
    return render_template('addquestion.html', form=form)


@user.route('/add-class', methods=['GET', 'POST'])
def add_class():
    form = AddGrade()
    if form.validate_on_submit():
        name = form.name.data
        grade = Grade(name=name)
        grade.save()
        # return redirect(url_for('user.home'))
    return render_template('addclass.html', form=form)


@user.route('/add-subject', methods=['GET', 'POST'])
def add_subject():
    form = AddSubject()
    if form.validate_on_submit():
        name = form.name.data
        subject = Subject(name=name)
        subject.save()
        # return redirect(url_for('user.home'))
    return render_template('addsubject.html', form=form)


@user.route('/reads', methods=['GET'])
def reads():
    filename = os.path.join(current_app.root_path, 'static')
    send_from_directory(filename, 'data.json')
    return redirect(url_for('user.home'))
