from dao.performance_dao import PerformanceDAO


class PerformanceService:

    def __init__(self):
        self.performance_dao = PerformanceDAO()

    def add_performance(self, performance):

        if performance.user_id is None:
            print("user id is required")
            return

        if performance.activity_id is None:
            print("activity id is required")
            return

        if performance.score is None:
            print("score is required")
            return

        if performance.score < 0 or performance.score > 100:
            print("score must be between 0 and 100")
            return

        if performance.mistake_count is None or performance.mistake_count < 0:
            print("mistake count cannot be negative")
            return

        self.performance_dao.add_performance(performance)

        print("performance added successfully")
    def get_performance_history(self, user_id):

        return self.performance_dao.get_performance_history(user_id)
    def get_daily_progress(self, user_id):

        return self.performance_dao.get_daily_progress(user_id)