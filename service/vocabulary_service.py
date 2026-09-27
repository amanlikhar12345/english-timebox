from dao.vocabulary_dao import VocabularyDAO


class VocabularyService:

    def __init__(self):
        self.vocabulary_dao = VocabularyDAO()

    def get_vocabulary_by_content(self, content_id):
        return self.vocabulary_dao.get_vocabulary_by_content(content_id)