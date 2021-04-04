from flask import g, make_response, request, url_for
from .routes import student
from .lowlevel import LowerLevelMenu
from .selectclass import SelectClassMenu
from .selectsubject import SelectSubjectMenu
from .register import RegistrationMenu
from .showanswers import ShowAnswersMenu
from .answerquestions import AnswerQuestionsMenu
from somo.models import AnonymousUser


@student.route('/student', methods=['POST', 'GET'])
def index():
    response = make_response("END connection ok")
    response.headers['Content-Type'] = "text/plain"
    return response


@student.route('/ussd/callback', methods=['POST', 'GET'])
def ussd_callback():
    """Handles post call back from AT"""
    session_id = g.session_id
    user = g.current_user
    session = g.session
    user_response = g.user_response
    if isinstance(user, AnonymousUser):
        # register user
        menu = RegistrationMenu(session_id=session_id, session=session, phone_number=g.phone_number,
                                user_response=user_response, user=user)
        return menu.execute()
    level = session.get('level')
    if level < 2:
        menu = LowerLevelMenu(session_id=session_id, session=session, phone_number=g.phone_number,
                              user_response=user_response, user=user)
        return menu.execute()
    if level == 2:
        """Select Class"""
        menu = SelectClassMenu(session_id=session_id, session=session, phone_number=g.phone_number,
                               user_response=user_response, user=user)
        return menu.execute()

    if level in [3, 30]:
        """Select Subject"""
        menu = SelectSubjectMenu(session_id=session_id, session=session, phone_number=g.phone_number,
                                 user_response=user_response, user=user, level=level)
        return menu.execute()

    if level in [4, 40]:
        """Answer Questions"""
        menu = AnswerQuestionsMenu(session_id=session_id, session=session, phone_number=g.phone_number,
                                   user_response=user_response, user=user, level=level)
        return menu.execute()

    if level == 5:
        """Show Answers"""
        menu = ShowAnswersMenu(session_id=session_id, session=session, phone_number=g.phone_number, user_response=user_response,
                               user=user, level=level)
        return menu.execute()

    # if level == 6:
    #     """Ask if they want to retake"""
    #     menu = ReinviteMenu(session_id=session_id, session=session, phone_number=g.phone_number, user_response=user_response,
    #                         user=user, level=level)
    #     return menu.execute()

    response = make_response(
        "END Thank you for interacting with our app. We hope to see you back soon\n", 200)
    response.headers['Content-Type'] = "text/plain"
    return response
