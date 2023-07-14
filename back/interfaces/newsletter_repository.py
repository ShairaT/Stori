from abc import ABC, abstractmethod

class NewsletterRepository(ABC):
    @abstractmethod
    def create_newsletter(self, title, author, image_file, description, subscribers=None):
        pass

    @abstractmethod
    def get_newsletter(self, newsletter_id):
        pass

    @abstractmethod
    def get_newsletters(self):
        pass

    @abstractmethod
    def update_newsletter(self, newsletter_id, title=None, author=None, image_file=None, description=None, subscribers=None):
        pass

    @abstractmethod
    def delete_newsletter(self, newsletter_id):
        pass