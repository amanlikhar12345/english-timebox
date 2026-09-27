from database.connection import Database


class PerformanceDAO:

    def add_performance(self, performance):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """
        insert into performance
        (user_id, activity_id, score, mistake_count, performance_date)
        values (%s, %s, %s, %s, %s)
        """

        values = (
            performance.user_id,
            performance.activity_id,
            performance.score,
            performance.mistake_count,
            performance.performance_date
        )

        cursor.execute(query, values)

        conn.commit()

        cursor.close()
        conn.close()

    def get_performance_history(self, user_id):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """
        select
            p.performance_date,
            a.activity_name,
            p.score,
            p.mistake_count
        from performance p
        join activities a
        on p.activity_id = a.activity_id
        where p.user_id = %s
        order by p.performance_date desc
        """

        cursor.execute(query, (user_id,))

        performance = cursor.fetchall()

        cursor.close()
        conn.close()

        return performance
    
    def get_daily_progress(self, user_id):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """select p.performance_date, a.activity_name, p.score, p.mistake_count from performance p join activities a on p.activity_id = a.activity_id where p.user_id = %s order by p.performance_date desc, p.performance_id desc """

        cursor.execute(query, (user_id,))

        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result