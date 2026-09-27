from database.connection import Database


class ReadingDAO:

    def get_all_content(self):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = "select * from reading_content"
        cursor.execute(query)

        content = cursor.fetchall()

        cursor.close()
        conn.close()

        return content