# the views should be put here
from flask import Blueprint, render_template, jsonify, request

home_blueprint = Blueprint('users', __name__, template_folder='../templates/')


@home_blueprint.route('/home')
def home():
    return render_template('other/index.html', title='home')


@home_blueprint.route('/about')
def about():
    return render_template('other/about.html', title='about')


@home_blueprint.route('/work/api')
def api():
    return jsonify({
        'hello': 'welcome'
    })


@home_blueprint.route('/register/api')
def register_api():
    if request.method == 'GET':
        pass

    else:
        pass


@home_blueprint.route('/blog')
def blog():
    return render_template('other/blog.html', title='blog')


@home_blueprint.route('/register')
def register():
    return render_template('other/register.html', title='register')


@home_blueprint.route('/login')
def login():
    return render_template('other/login.html', title='login')


@home_blueprint.route('/logout')
def logout():
    return 'you are logged out'
