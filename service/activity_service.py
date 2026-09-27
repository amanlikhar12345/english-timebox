
from dao.activity_dao import ActivityDAO


class ActivityService:

    def __init__(self):
        self.activity_dao = ActivityDAO()

    def get_all_activities(self):
        return self.activity_dao.get_all_activities()