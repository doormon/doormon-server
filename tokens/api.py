""" api routes
"""

from google.appengine.api import users
import hashlib, random

from website import app
from .decorators import login_required
from .models import User


def gen_api_key():
    hashlib.sha224(str(random.getrandbits(256))).hexdigest();


@app.route('/register/mobile/<registration_id>/')
@login_required
def register_mobile(registration_id):
    user = User.get_by_user(users.get_current_user())
    user.registration_id = registration_id
    user.api_key = gen_api_key()
    user.put()
    return """Registered device against Google account. Visit <a
    href="https://doormon-server.appspot.com/key/">
    https://doormon-server.appspot.com/key/</a> to retrieve the API key for the
    Raspberry Pi."""
