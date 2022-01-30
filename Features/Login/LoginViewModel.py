from DBService.MYSQLService import MYSQLService
from Utils.Widgets.DialogProvider import DialogProvider
import re


class LoginViewModel:

    def __init__(self, db_service: MYSQLService, user_logged_in):
        self._user_logged_in = user_logged_in
        self._db_service = db_service
        self.get_user_email = None
        self.get_password = None

    def login_button_clicked(self):

        email = self.get_user_email()
        password = self.get_password()

        if email is None or len(email) == 0:
            DialogProvider.present_error("fill email", "Error")
            return
        if password is None or len(password) == 0:
            DialogProvider.present_error("fill password", "Error")
            return

        email = re.sub(r"[\n\t\s]*", "", email)
        password = re.sub(r"[\n\t\s]*", "", password)

        query = "SELECT username,password from User where username " \
                "like '" + email + "'and password like '" \
                + password + "'"
        result = self._db_service.fetch_one(query)

        print(result)

        if result is None:
            DialogProvider.present_error_modal("Incorrect email or password", "Error")
        else:
            DialogProvider.present_error_modal("You are logged in", "Success")
            self._user_logged_in()
