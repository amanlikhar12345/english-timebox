from database.connection import Database


class MistakeDAO:

    def add_mistake(self, mistake):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """insert into mistakes (user_id, activity_id, mistake_type, mistake_text, correct_text, mistake_date) values (%s, %s, %s, %s, %s, %s)"""

        values = (mistake.user_id,mistake.activity_id,mistake.mistake_type,mistake.mistake_text,mistake.correct_text,mistake.mistake_date)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()