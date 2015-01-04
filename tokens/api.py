""" api routes
"""

from google.appengine.api import users, urlfetch
from flask import jsonify, request

import json

from website import app
from .decorators import login_required
from .models import User, Config


def get_gcm_api_key():
    return Config.get_config().api_key


@app.route('/register/mobile/<registration_id>/')
@login_required
def register_mobile(registration_id):
    user = User.get_by_user(users.get_current_user())
    user.registration_id = registration_id
    user.put()
    return """Registered device against Google account. Visit <a
    href="https://doormon-server.appspot.com/key/">
    https://doormon-server.appspot.com/key/</a> to retrieve the API key for the
    Raspberry Pi."""


@app.route('/api/push/', methods = [ 'POST' ])
def push_state():
    key = request.form.get('api_key', None)
    if key is None:
        return jsonify(error='No API key')
    user = User.get_by_api_key(key)
    if user is None:
        return jsonify(error='Invalid API key')

    state = request.form.get('state', 'invalid')
    video_uri = request.form.get('video_uri', '')

    result = urlfetch.fetch(
            method=urlfetch.POST,
            url=app.config['GCM_ENDPOINT'],
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'key=%s' % get_gcm_api_key()
                },
            payload=json.dumps({
                'registration_ids': [ user.registration_id ],
                'data': {
                    'type': 'door',
                    'state': state,
                    'video_uri': video_uri
                    }
                }))

    return jsonify(success=result.status_code == 200,
            result=json.loads(result.content))
