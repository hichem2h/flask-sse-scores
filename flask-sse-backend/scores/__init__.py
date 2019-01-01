from flask import Blueprint

bp = Blueprint('scores', __name__, template_folder='templates')

from .views import *
