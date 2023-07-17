import magic
import requests

def get_file_type(url):
        response = requests.get(url)
        primeros_bytes = response.content[:4096]  # Leer los primeros 4096 bytes

        # Utilizar python-magic para determinar el tipo de archivo basado en los primeros bytes
        tipo_archivo = magic.from_buffer(primeros_bytes, mime=True)

        return tipo_archivo