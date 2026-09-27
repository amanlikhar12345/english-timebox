
from dao.reading_dao import ReadingDAO


class ReadingService:

    def __init__(self):
        self.reading_dao = ReadingDAO()

    def get_all_content(self):
        return self.reading_dao.get_all_content()