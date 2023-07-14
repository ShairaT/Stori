

from back.implementations.email_sender import EmailSender

class NewsletterEmailService:
    def __init__(self):
        self.email_sender = EmailSender()

    def send_article_email(self, subscriber_email, article):
        subject = article.get("subject")
        body = f'Hola,\n\nAquí tienes la información del nuevo artículo:\n\n{article.get("subject")}'
        self.email_sender.send_email(subscriber_email, subject, body, article.get("article_url_path"))