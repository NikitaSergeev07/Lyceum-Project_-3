import sqlalchemy

from .db_session import SqlAlchemyBase


class Contact_form(SqlAlchemyBase):
    __tablename__ = 'contact'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    message = sqlalchemy.Column(sqlalchemy.String)
