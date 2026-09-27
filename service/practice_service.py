from dao.practice_dao import PracticeDAO


class PracticeService:

    def __init__(self):
        self.practice_dao = PracticeDAO()

    def add_practice(self, practice):
        if practice.user_id is None:
            print("user id is required")
            return

        if practice.activity_id is None:
            print("activity id is required")
            return

        if practice.planned_minutes is None or practice.planned_minutes <= 0:
            print("planned minutes must be greater than 0")
            return

        if practice.actual_minutes is None or practice.actual_minutes < 0:
            print("actual minutes cannot be negative")
            return

        if practice.actual_minutes > practice.planned_minutes:
            print("actual minutes cannot be greater than planned minutes")
            return

        if practice.status not in ["completed", "pending"]:
            print("invalid status")
            return

        self.practice_dao.add_practice(practice)
        print("practice added successfully")