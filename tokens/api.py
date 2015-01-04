""" api routes
"""

from google.appengine.api import users

from website import app
from .decorators import login_required
from .models import User

@app.route('/register/mobile/<registration_id>/')
@login_required
def register_mobile(registration_id):
    user = User.get_by_user(users.get_current_user())
    user.registration_id = registration_id
    user.put()
    return "Registered device against Google account"
