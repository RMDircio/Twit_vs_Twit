
from flask import Blueprint

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/')
def index():
    return 'Welcome User'

@user_routes.route('/aboutus')
def about():
    print('Here is the About Us page')
    return 'About Us'