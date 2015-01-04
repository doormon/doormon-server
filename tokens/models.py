from google.appengine.ext import ndb

import hashlib, random

def gen_api_key():
    return hashlib.sha224(str(random.getrandbits(256))).hexdigest()


class Config(ndb.Model):
    api_key = ndb.StringProperty(required=False)

    @classmethod
    def get_config(cls):
        entity = Config.query().get()
        if entity is None:
            entity = Config()
            entity.put()
        return entity


class User(ndb.Model):
    user = ndb.UserProperty(required=True)
    registration_id = ndb.StringProperty(required=False)
    api_key = ndb.StringProperty(required=False)

    @classmethod
    def get_by_user(cls, user):
        entity = User.query(User.user == user).get()
        if entity is None:
            entity = User(user=user)
            entity.api_key = gen_api_key()
            entity.put()
        return entity

    @classmethod
    def get_by_api_key(cls, api_key):
        return User.query(User.api_key == api_key).get()
