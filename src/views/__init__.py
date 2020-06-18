# the views should be put here
import requests
from flask import Blueprint, render_template, jsonify, request
import pygal

home_blueprint = Blueprint('users', __name__, template_folder='../templates/')


@home_blueprint.route('/home')
def home():
    try:
        data = requests.get('https://api.exchangeratesapi.io/2001-01-12')
        ex = data.json()
        canad_001 = ex['rates']['CAD']
        HKD_001 = ex['rates']['HKD']
        CYP_001 = ex['rates']['CYP']
        GBP__001= ex['rates']['GBP']

        data_2002 = requests.get('https://api.exchangeratesapi.io/2002-01-12')
        f_data = data_2002.json()
        canad_002 = f_data['rates']['CAD']
        HKD_002 = f_data['rates']['HKD']
        CYP_002 = f_data['rates']['CYP']
        GBP__002= f_data['rates']['GBP']

        data_2003 = requests.get('https://api.exchangeratesapi.io/2003-01-12')
        f01_data = data_2003.json()
        canad_003 = f01_data['rates']['CAD']
        HKD_003 = f01_data['rates']['HKD']
        CYP_003 = f01_data['rates']['CYP']
        GBP__003= f01_data['rates']['GBP']

        data_2004 = requests.get('https://api.exchangeratesapi.io/2004-01-12')
        f02_data = data_2004.json()
        canad_004 = f02_data['rates']['CAD']
        HKD_004 = f02_data['rates']['HKD']
        CYP_004 = f02_data['rates']['CYP']
        GBP__004= f02_data['rates']['GBP']

        data_2005 = requests.get('https://api.exchangeratesapi.io/2004-01-12')
        f03_data = data_2005.json()
        canad_005 = f03_data['rates']['CAD']
        HKD_005 = f03_data['rates']['HKD']
        CYP_005 = f03_data['rates']['CYP']
        GBP__005 = f03_data['rates']['GBP']

        line_chart = pygal.Bar()
        line_chart.title = 'changes in usd from the year 2001 to 2005 in euros'
        line_chart.x_labels = map(str, range(2001, 2006))
        line_chart.add('CAD', [canad_001, canad_002, canad_003, canad_004, canad_005])
        line_chart.add('HKD', [HKD_001, HKD_002, HKD_003, HKD_004, HKD_005])
        line_chart.add('CYP', [CYP_001, CYP_002, CYP_003, CYP_004, CYP_005])
        line_chart.add('GBP', [GBP__001, GBP__002, GBP__003, GBP__004, GBP__005])
        graph_data = line_chart.render_data_uri()
        return render_template('other/index.html', title='home', graph_data=graph_data, data=data.json())
    except Exception as e:
        return (str(e))


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
