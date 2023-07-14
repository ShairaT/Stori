from back.interfaces.user_repository import UsersRepository


class UserService:
    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    def register_user(self, email, password):
        # Agrega la lógica de validación y cualquier otra operación necesaria antes del registro
        return self.users_repository.create_user(email, password)

    def login_user(self, email, password):
            return self.users_repository.login_user(email, password)
    # Agrega otros métodos según sea necesario