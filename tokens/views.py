from website import app
from models import Config

from google.appengine.api import users

from flask import request, render_template

from .decorators import admin_login_required, login_required

from .models import User

@app.route('/')
def root():
    return "Doormon server"


@app.route('/admin/', methods = [ 'GET', 'POST' ])
@admin_login_required
def admin():
    if request.method == 'POST':
        api_key = request.form.get('api_key', None)
        if api_key is None:
            return render_template('admin/admin.html', fail=True)
        config = Config.get_config()
        config.api_key = api_key
        config.put()
    return render_template('admin/admin.html')


@app.route('/test/', methods = [ 'GET' ])
@login_required
def test():
    user = User.get_by_user(users.get_current_user())
    api_key = user.api_key
    return render_template('test/test.html', api_key=api_key)


@app.route('/key/', methods = [ 'GET' ])
@login_required
def key():
    user = User.get_by_user(users.get_current_user())
    api_key = user.api_key
    return render_template('key/key.html', api_key=api_key)
