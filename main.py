# methods: class, object, static
from pprint import pprint
from hashlib import sha256
from uuid import uuid1
from json import dumps


class User:

    def __init__(self, email, password=None, id=None):
        if self.is_valid_email(email):
            self.id = id or uuid1()
            self.email = email
            self.hash_password = password or self.hash_password(password)
        else:
            raise ValueError('email xato')

    def to_json(self) -> dict:
        return {
            "id": str(self.id),
            "email": self.email,
            "hash_password": self.hash_password,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(id=data['id'], email=data['email'], password=data['hash_password'])

    @staticmethod
    def is_valid_email(email):
        return '@' in email

    @staticmethod
    def hash_password(password):
        return sha256(password.encode()).hexdigest()


data = {"id": "efc60f08-d6cc-11f1-8395-1e178c57142a", "email": "ali@gmail.com", "hash_password": "bkfjsdbafijb4i32534t23s"}

user = User.from_dict(data)

print(user.email)

