from database.connection import Database


class VocabularyDAO:

    def get_vocabulary_by_content(self, content_id):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """select vocabulary_id, word, meaning, example_sentencefrom vocabularywhere content_id = %s"""

        cursor.execute(query, (content_id,))

        vocabulary = cursor.fetchall()

        cursor.close()
        conn.close()

        return vocabulary