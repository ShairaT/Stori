from back.adapters.firebase_adapter import register_user, login_user


class UsersRepositoryImpl:
    def get_user_by_email(self, email):
        # Implementa la lógica para obtener el usuario por correo electrónico
        raise NotImplementedError

    def create_user(self, email, password):
        return register_user(email, password)

    def login_user(self, email, password):
        return login_user(email, password)

    # Agrega otros métodos según sea necesario