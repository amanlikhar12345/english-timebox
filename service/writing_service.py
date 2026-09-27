from dao.writing_dao import WritingDAO


class WritingService:

    def __init__(self):

        self.writing_dao = WritingDAO()

    def add_writing(self, user_id, content_id, response):

        self.writing_dao.add_writing(user_id,content_id,response)