from ..base_menu import Menu
from .utils import grades, subjects


class SelectClassMenu(Menu):
    def select_subject(self):  # 50
        grade = self.user_response
        self.session['grade'] = grades.get(int(grade))

        menu_text = "Select Subject:-\n"
        for i, j in subjects.items():
            menu_text += f"{i}. {j}\n"
        self.session['level'] = 3
        return self.ussd_proceed(menu_text)

    def execute(self):
        print("level2", self.level, self.session)
        menu = {
            2: self.select_subject,
        }
        return menu.get(self.session['level'])()
