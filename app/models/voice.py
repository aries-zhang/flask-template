import time  # NOQA
from app import db


class Voice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    content = db.Column(db.String)
    createtime = db.Column(db.DateTime)

    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.createtime = time.time()
