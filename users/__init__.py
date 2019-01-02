from flask import Blueprint


users_blu = Blueprint("users",__name__)

from . import views
