from back.interfaces.newsletter_repository import NewsletterRepository

class NewsletterService:
    def __init__(self, newsletter_repository: NewsletterRepository):
        self.newsletter_repository = newsletter_repository

    def create_newsletter(self, title, author, image_file, description, subscribers=None):
        # Lógica de validación y operaciones adicionales
        return self.newsletter_repository.create_newsletter(title, author, image_file, description, subscribers)

    def get_newsletter(self, newsletter_id):
        # Lógica para obtener un newsletter
        return self.newsletter_repository.get_newsletter(newsletter_id)

    def get_newsletters(self):
        # Lógica para obtener un newsletter
        return self.newsletter_repository.get_newsletters()

    def update_newsletter(self, newsletter_id, title=None, author=None, image_file=None, description=None, subscribers=None):
        # Lógica para actualizar un newsletter
        return self.newsletter_repository.update_newsletter(newsletter_id, title, author, image_file, description, subscribers)

    def delete_newsletter(self, newsletter_id):
        # Lógica para eliminar un newsletter
        return self.newsletter_repository.delete_newsletter(newsletter_id)