# methods: class, object, static

from hashlib import sha256


class User:

    def __init__(self, email, password):
        if self.is_valid_email(email):
            self.email = email
            self.hash_password = self.hash_password(password)
        else:
            raise ValueError('email xato')

    @staticmethod
    def is_valid_email(email):
        return '@' in email

    @staticmethod
    def hash_password(password):
        return sha256(password.encode()).hexdigest()


user = User('ali@gamil.com', '123')

