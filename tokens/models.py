from google.appengine.ext import ndb

class User(ndb.Model):
	user = ndb.UserProperty(required=True)
	registration_id = ndb.StringProperty(required=False)
    api_key = ndb.StringProperty(required=False)

    @classmethod
    def get_by_user(cls, user):
        entity = User.query(User.user == user).get()
        if entity is None:
            entity = User(user=user)
            entity.put()
        return entity
