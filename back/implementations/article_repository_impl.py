from back.interfaces.article_repository import ArticleRepository
from config.firebase_config import db, storage
import uuid

class FirebaseArticleRepository(ArticleRepository):
    def create_article(self, subject, article_file, newsletter_id, schedule_time=None):
        article_id = str(uuid.uuid4())
        storeFilePath = "articles/" + article_id
        image_ref = storage().child(storeFilePath)
        image_ref.put(article_file)
        url = storage().child(storeFilePath).get_url(None)

        article = {
            "uuid": article_id,
            "subject": subject,
            "newsletter_id": newsletter_id,
            "article_url_path": url,
            "schedule_time": None
        }
        if schedule_time is not None:
            article["schedule_time"] = schedule_time

        db.child("articles/" + article_id).set(article)
        return article_id

    def get_article(self, article_id):
        article = db.child("articles").child(article_id).get().val()
        return article

    def get_articles(self):
        articles = db.child("articles").get().val()
        if articles:
            return list(articles.values())
        return []

    def update_article(self, article_id, subject=None, article_file=None, newsletter_id=None, schedule_time=None):
        article = db.child("articles").child(article_id).get().val()

        if article:
            if subject:
                article["subject"] = subject
            if newsletter_id:
                article["newsletter_id"] = newsletter_id
            if schedule_time:
                article["schedule_time"] = schedule_time

            if article_file:
                storeFilePath = "articles/" + article_id
                image_ref = storage().child(storeFilePath)
                image_ref.put(article_file)
                url = storage().child(storeFilePath).get_url(None)

                article["image_url"] = url

            db.child("articles").child(article_id).update(article)

            return True
        else:
            return False

    def delete_article(self, article_id):
        db.child("articles").child(article_id).remove()

        return True
