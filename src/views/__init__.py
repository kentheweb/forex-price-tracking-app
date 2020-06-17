# the views should be put here
from flask import Blueprint, render_template

home_blueprint = Blueprint('users', __name__, template_folder='../templates/')


@home_blueprint.route('/home')
def home():
    return render_template('other/index.html')


@home_blueprint.route('/about')
def about():
    return render_template('other/about.html')



