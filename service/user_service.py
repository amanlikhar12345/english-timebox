from dao.user_dao import UserDAO


class UserService:

    def __init__(self):
        self.user_dao = UserDAO()

    def add_user(self, user):
        if user.name == "":
            print("name cannot be empty")
            return

        if user.email == "":
            print("email cannot be empty")
            return

        self.user_dao.add_user(user)
        print("user added successfully")