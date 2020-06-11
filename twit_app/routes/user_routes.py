
from flask import Blueprint, render_template

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/')
def index():
    return render_template('prediction_form.html')

@user_routes.route('/aboutus')
def about():
    print('Here is the About Us page')
    return 'About Us'