from ..base_menu import Menu
from ..models import Student
from flask import current_app


class RegistrationMenu(Menu):
    """Serves registration callbacks"""

    def get_number(self):
        # insert user's phone number
        self.session["level"] = 21
        menu_text = f"Welcome To { current_app.config['APP_NAME']}. To register enter your names:-"
        return self.ussd_proceed(menu_text)

    def get_username(self):
        username = self.user_response
        # check if user entered an option or username exists
        if username:
            f_name, l_name = username.split()
            self.user = Student.create(
                first_name=f_name, last_name=l_name, phone_number=self.phone_number)
            print(self.user)
            self.session["level"] = 0
            # go to home
            return self.home()
        else:  # Request again for name - level has not changed...
            menu_text = "Wrong username. Please enter your names:- \n"
            return self.ussd_proceed(menu_text)

    def execute(self):
        if self.session["level"] == 0:
            return self.get_number()
        else:
            return self.get_username()
