from database.connection import Database


class WritingDAO:

    def add_writing(self, user_id, content_id, response):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """insert into writing(user_id, content_id, response)values (%s, %s, %s)"""

        values = (user_id,content_id,response)

        cursor.execute(query, values)

        conn.commit()

        cursor.close()
        conn.close()