class UsersRepository:
    def get_user_by_email(self, email):
        raise NotImplementedError

    def create_user(self, email, password):
        raise NotImplementedError

    def login_user(self, email, password):
        raise NotImplementedError

    # Agrega otros métodos según sea necesario