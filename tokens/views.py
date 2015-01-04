from website import app
from models import Config

from flask import request, render_template

from .decorators import admin_login_required

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
