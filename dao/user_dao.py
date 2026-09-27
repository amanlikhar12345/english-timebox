from database.connection import Database


class UserDAO:

    def add_user(self, user):
        db = Database()
        conn=db.connect()
        cursor = conn.cursor()

        query = "insert into users (name, email) values (%s, %s)"
        values = (user.name, user.email)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()
        



