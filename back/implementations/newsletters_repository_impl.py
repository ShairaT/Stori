from back.interfaces.newsletter_repository import NewsletterRepository
from config.firebase_config import db, storage
import uuid

class FirebaseNewsletterRepository(NewsletterRepository):
    def create_newsletter(self, title, author, image_file, description, subscribers=None):
        newsletter_id = str(uuid.uuid4())
        storeFilePath = "newsletters/" + newsletter_id
        # Guardar la imagen demostrativa en el almacenamiento de Firebase
        image_ref = storage().child(storeFilePath)
        image_ref.put(image_file)
        url = storage().child(storeFilePath).get_url(None)

        # Crear el objeto de newsletter con los atributos proporcionados
        newsletter = {
            "uuid": newsletter_id,
            "title": title,
            "author": author,
            "image_url_path": url,
            "description": description,
            "subscribers": []
        }
        print(subscribers)
        if subscribers is not None:
            newsletter["subscribers"] = subscribers

        # Guardar el newsletter en la base de datos
        db.child("newsletters/" + newsletter_id).set(newsletter)
        # Devolver el ID del newsletter creado
        return newsletter_id

    def get_newsletter(self, newsletter_id):
        # Obtener el newsletter de la base de datos por su ID
        newsletter = db.child("newsletters").child(newsletter_id).get().val()
        return newsletter

    def get_newsletters(self):
        # Obtener todos los nwesletters
        newsletters = db.child("newsletters").get().val()
        if newsletters:
            return list(newsletters.values())
        return []

    def update_newsletter(self, newsletter_id, title=None, author=None, image_file=None, description=None, subscribers=None):
        # Obtener el newsletter de la base de datos por su ID
        newsletter = db.child("newsletters").child(newsletter_id).get().val()

        if newsletter:
            # Actualizar los atributos proporcionados
            if title:
                newsletter["title"] = title
            if author:
                newsletter["author"] = author
            if description:
                newsletter["description"] = description
            if subscribers is not None:
                print(subscribers)
                newsletter["subscribers"] = subscribers

            if image_file:
                storeFilePath = "newsletters/" + newsletter_id
                # Guardar la nueva imagen demostrativa en el almacenamiento de Firebase
                image_ref = storage().child(storeFilePath)
                image_ref.put(image_file)
                url = storage().child(storeFilePath).get_url(None)

                # Actualizar la URL de la imagen demostrativa
                newsletter["image_url"] = url

            # Actualizar el newsletter en la base de datos
            db.child("newsletters").child(newsletter_id).update(newsletter)

            return True
        else:
            return False

    def delete_newsletter(self, newsletter_id):
        # Eliminar el newsletter de la base de datos por su ID
        db.child("newsletters").child(newsletter_id).remove()

        return True
