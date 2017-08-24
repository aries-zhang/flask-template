from flask import Flask, render_template  # NOQA import flask and template operators
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__, static_folder='assets')

# Configurations
app.config.from_object('config')

# Set asset bundles
assets = Environment(app)

css = Bundle('lib/bootstrap/dist/css/bootstrap.css',
             'css/admin.css',
             filters='cssmin',
             output='dist/site.css')

bundles = {'admin_css': Bundle('lib/bootstrap/dist/css/bootstrap.css',
                               'css/admin.css',
                               filters='cssmin',
                               output='dist/site.css'),
           'admin_js': Bundle('lib/bootstrap/dist/js/bootstrap.js',
                              'js/admin.js',
                              filters='jsmin',
                              output='dist/site.js')
           }

assets.register(bundles)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error(error):
    return render_template('500.html'), 500


from controllers.home import *  # NOQA
from controllers.blog import *  # NOQA
from controllers.user import *  # NOQA
from models.article import *  # NOQA
from models.category import *  # NOQA
from models.comment import *  # NOQA
from models.link import *  # NOQA
from models.user import *  # NOQA
from models.voice import *  # NOQA

# Register blueprint(s)
from admin.controllers import admin as admin_module  # NOQA
app.register_blueprint(admin_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()
