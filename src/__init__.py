from flask import Flask


app = Flask(__name__)

from .views import home_blueprint

app.register_blueprint(home_blueprint, url_prefix='/user')
