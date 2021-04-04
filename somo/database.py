from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

from .util import kenya_time
from somo import redis, db


class CRUDMixin(object):
    def __repr__(self):
        return "<{}>".format(self.__class__.__name__)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def save(self):
        """Saves object to database"""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """deletes object from db"""
        db.session.delete(self)
        db.session.commit()
        return self
