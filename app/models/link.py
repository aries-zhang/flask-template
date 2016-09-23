import time  # NOQA
from app import db


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    url = db.Column(db.String)
    description = db.Column(db.String)
    type = db.Column(db.Integer)
    enabled = db.Column(db.Boolean)
    createtime = db.Column(db.DateTime)

    def __init__(self, title, url, description, type, enabled):
        self.title = title
        self.url = url
        self.description = description
        self.type = type
        self.enabled = enabled
        self.createtime = time.time()
