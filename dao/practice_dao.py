from database.connection import Database


class PracticeDAO:

    def add_practice(self, practice):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """insert into practice (user_id, activity_id, practice_date, planned_minutes, actual_minutes, status) values (%s, %s, %s, %s, %s, %s) """

        values = (practice.user_id,practice.activity_id,practice.practice_date,practice.planned_minutes,practice.actual_minutes,practice.status)

        cursor.execute(query,values)
        conn.commit()

        cursor.close()
        conn.close()