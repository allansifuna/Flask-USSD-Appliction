from somo import create_app
create_app().app_context().push()
from somo.models import ExamQuestion, Grade, Subject
import os
import json


def add_all():
    a = ["Class One", "Class Two", "Class Three", "Class Four",
         "Class Five", "Class Six", "Class Seven", "Class Eight"]
    for i in a:
        s = Grade(name=i)
        s.save()

    b = ['English', 'Mathematics', 'Kiswahili',
         'Science', 'Social Studies', 'C.R.E', 'I.R.E']
    for i in b:
        v = Subject(name=i)
        v.save()
    return True


def read():
    quizes = ExamQuestion.query.all()
    quests = []
    for quiz in quizes:
        quiz_obj = {}
        quiz_obj['question'] = quiz.question
        quiz_obj['option_A'] = quiz.option_A
        quiz_obj['option_B'] = quiz.option_B
        quiz_obj['option_C'] = quiz.option_C
        quiz_obj['option_D'] = quiz.option_D
        quiz_obj['explanation'] = quiz.explanation
        quiz_obj['answer'] = quiz.answer
        quiz_obj['subjectquestion'] = quiz.subjectquestion.name
        quiz_obj['gradequestion'] = quiz.gradequestion.name
        quests.append(quiz_obj)
    return quests


def write():
    data = read()
    file = os.path.abspath(os.path.dirname(
        __file__)) + '/somo/static/data.json'
    print(file)
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
    return True
