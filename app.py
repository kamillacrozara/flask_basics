from flask import Flask, g
from flask.ext.login import LoginManager

import models

DEBUG = True

app = Flask(__name__)
app.secret_key = 'A098S09AShuaIAS#)(90!#+)*(98s+)a(d_)(@!#89-0'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """ Connect to database before each request"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request"""
    g.db.close()
    return response


if __name__ == '__main__':
    models.initialize()
    models.User.create_user(
        name='kennethlove',
        email='kenneth@treehouse.com',
        password='password',
        admin=True
        )
    app.run(debug=DEBUG)
