import sqlalchemy as sa
from database import db

class User(db.Model):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(80), unique=True, nullable=False)
    password = sa.Column(sa.String(120), nullable=False)

    def __repr__(self):
        return f'User {self.username}'