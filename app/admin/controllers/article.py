from flask import render_template
from app.admin.controllers import admin
from app import db


@admin.route('/signin/')
def signin():
    return 'this is admin signin page'


@admin.route('/articles')
def list():
    return render_template('admin/article/list.html')


@admin.route('/article/add')
def add():
    return render_template('admin/article/edit.html')
