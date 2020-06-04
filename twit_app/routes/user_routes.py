
from flask import Blueprint

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/')
def index():
    print('Your User Page')
    x = 2 + 3
    return f'Welcome User: {x}'

@user_routes.route('/aboutus')
def about():
    print('Here is the About Us page')
    return 'About Us'