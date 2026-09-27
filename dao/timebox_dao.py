from database.connection import Database


class TimeboxDAO:

    def get_today_timebox(self, user_id):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """select t.timebox_id,t.activity_id,a.activity_name,t.recommended_minutes,t.timebox_date from timebox t join activities a on t.activity_id = a.activity_id where t.user_id = %s and t.timebox_date = curdate() order by t.activity_id """

        cursor.execute(query,(user_id,))

        timebox = cursor.fetchall()

        cursor.close()
        conn.close()

        return timebox