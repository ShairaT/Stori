from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
from utils.convert_url_firebase_to_base64 import convert_url_firebase_to_base64
from utils.get_file_type import get_file_type
from dotenv import load_dotenv
import os

load_dotenv()

class EmailSender:
    def __init__(self):
        self.sg = SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))

    def send_email(self, recipient_email, subject, body, article_file_path):
        # Crear el objeto del mensaje
        mail = Mail(
        from_email='ayelenmaite2000@gmail.com',
        to_emails=recipient_email,
        subject=subject,
        plain_text_content=body)

        file_type = get_file_type(article_file_path)
        image_content_base64 = convert_url_firebase_to_base64(article_file_path)

        # Adjunta el archivo al correo electrónico
        attachment = Attachment()
        attachment.file_content = image_content_base64
        attachment.file_name = FileName('article')
        attachment.file_type = FileType(file_type)
        attachment.content_id = "image_cid"
        attachment.disposition = Disposition('attachment')
        mail.attachment = attachment

        # Envía el correo electrónico utilizando SendGrid
        response = self.sg.send(mail)

        if response.status_code == 202:
            return True
        else:
            return False


    