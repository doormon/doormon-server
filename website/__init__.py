from flask import Flask

app = Flask('doormon-server')
app.config.from_object('tokens.settings')

import tokens.api
