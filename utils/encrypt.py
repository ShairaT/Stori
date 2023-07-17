from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

encryption_key = os.getenv("ENCRYPTION_KEY")
cipher_suite = Fernet(encryption_key)

def encrypt_email(email):
    return cipher_suite.encrypt(email.encode()).decode()