""" main.py is the top level script.

"""

import os
import sys

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import render_template, redirect

from website import app
