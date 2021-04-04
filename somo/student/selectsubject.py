from ..base_menu import Menu
from .utils import subjects


class SelectSubjectMenu(Menu):
    def select_subject(self):  # 50
        subject = self.user_response
        self.session['subject'] = subjects.get(int(subject))

        menu_text = f"You are about to attempt 10 class {self.session.get('grade')} {self.session.get('subject')} questions :-\n"\
            "1. Continue\n"\
            "2. Back\n"
        self.session['level'] = 4
        return self.ussd_proceed(menu_text)

    def execute(self):
        menu = {
            3: self.select_subject
        }
        return menu.get(self.level)()
