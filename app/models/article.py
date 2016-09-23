import time  # NOQA
from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    key = db.Column(db.String)
    categoryid = db.Column(db.Integer)
    author = db.Column(db.String)
    weather = db.Column(db.Integer)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    hits = db.Column(db.Integer)
    createtime = db.Column(db.DateTime)

    def __init__(self, key, title, categoryid, author, weather, content):
        self.key = key
        self.title = title
        self.categoryid = categoryid
        self.author = author
        self.weather = weather
        self.content = content
        self.createtime = time.time()
