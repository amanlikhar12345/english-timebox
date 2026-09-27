class Practice:
    def __init__(self, practice_id, user_id, activity_id,planned_minutes, actual_minutes,practice_date, status):
        self.practice_id = practice_id
        self.user_id = user_id
        self.activity_id = activity_id
        self.planned_minutes = planned_minutes
        self.actual_minutes = actual_minutes
        self.practice_date = practice_date
        self.status = status