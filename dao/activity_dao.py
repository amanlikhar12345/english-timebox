from database.connection import Database


class ActivityDAO:

    def get_all_activities(self):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = "select * from activities"
        cursor.execute(query)

        activities = cursor.fetchall()

        cursor.close()
        conn.close()

        return activities