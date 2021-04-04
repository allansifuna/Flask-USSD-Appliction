from flask import Blueprint, request

student = Blueprint('student', __name__)
from . import view, decorators
