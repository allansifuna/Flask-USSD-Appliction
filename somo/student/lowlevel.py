from ..base_menu import Menu
from .utils import grades


class LowerLevelMenu(Menu):
    """serves the home menu"""

    def select_class(self):  # 1
        menu_text = "Select class:-\n"
        for i, j in grades.items():
            menu_text += f"{i}. {j}\n"
        self.session['level'] = 2
        return self.ussd_proceed(menu_text)

    def ask_questions(self):  # 2
        menu_text = "This part is under development, we hope to complete it soon\n"
        return self.ussd_end(menu_text)

    def execute(self):
        print("level", self.user_response)
        menus = {
            '1': self.select_class,
            '2': self.ask_questions,
        }
        return menus.get(self.user_response, self.home)()
