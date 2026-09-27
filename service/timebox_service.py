from dao.timebox_dao import TimeboxDAO


class TimeboxService:

    def __init__(self):
        self.timebox_dao = TimeboxDAO()

    def get_today_timebox(self, user_id):
        return self.timebox_dao.get_today_timebox(user_id)