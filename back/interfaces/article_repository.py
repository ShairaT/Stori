from abc import ABC, abstractmethod

class ArticleRepository(ABC):
    @abstractmethod
    def create_article(self, subject, article_file, newsletter_id, schedule_time=None):
        pass

    @abstractmethod
    def get_article(self, article_id):
        pass

    @abstractmethod
    def get_articles(self):
        pass

    @abstractmethod
    def update_article(self, article_id, subject=None, article_file=None, newsletter_id=None, schedule_time=None):
        pass

    @abstractmethod
    def delete_article(self, article_id):
        pass