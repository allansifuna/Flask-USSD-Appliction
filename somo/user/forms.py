from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField, SelectField, TextAreaField, \
    SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField


class AddGrade(FlaskForm):
  name = StringField('Class Name', validators=[
                     DataRequired()])


class AddSubject(FlaskForm):
  name = StringField('Subject Name', validators=[
                     DataRequired()])


class AddQuestion(FlaskForm):
  question = TextAreaField('Question', validators=[
      DataRequired(), Length(min=2)])
  option_A = StringField('Option A', validators=[
                         DataRequired()])
  option_B = StringField('Option B', validators=[
                         DataRequired()])
  option_C = StringField('Option C', validators=[
                         DataRequired()])
  option_D = StringField('Option D', validators=[
                         DataRequired()])
  answer = SelectField('Answer', choices=[(
      '', 'Select Correct Answer..'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
  explanation = TextAreaField('Explanation', validators=[Length(min=2)])
  subject = QuerySelectField(
      'Select Subject', validators=[], get_label='name', allow_blank=True)
  grade = QuerySelectField(
      'Select Class', validators=[], get_label='name', allow_blank=True)
