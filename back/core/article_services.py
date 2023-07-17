from back.interfaces.article_repository import ArticleRepository

class ArticleService:
    def __init__(self, article_repository: ArticleRepository):
        self.article_repository = article_repository

    def create_article(self, subject, article_file, newsletter_id, schedule_time=None):
        # Lógica de validación y operaciones adicionales
        return self.article_repository.create_article(subject, article_file, newsletter_id, schedule_time)

    def get_article(self, article_id):
        # Lógica para obtener un article
        return self.article_repository.get_article(article_id)

    def get_articles(self):
        # Lógica para obtener un article
        return self.article_repository.get_articles()

    def update_article(self, article_id, subject=None, article_file=None, newsletter_id=None, schedule_time=None):
        # Lógica para actualizar un article
        return self.article_repository.update_article(article_id, subject, article_file, newsletter_id, schedule_time)

    def delete_article(self, article_id):
        # Lógica para eliminar un article
        return self.article_repository.delete_article(article_id)