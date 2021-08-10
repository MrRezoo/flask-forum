from app import db
from app.database import BaseModel


class User(BaseModel):
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.id}, {self.username})'

