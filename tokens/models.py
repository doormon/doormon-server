from google.appengine.ext import ndb

class User(ndb.Model):
	user = ndb.UserProperty(required=True)
	registration_id = ndb.StringProperty(required=True)
        api_key = ndb.StringProperty(required=True)
