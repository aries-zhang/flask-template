import time  # NOQA
from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    articleid = db.Column(db.Integer)
    userid = db.Column(db.Integer)
    content = db.Column(db.String)
    ip = db.Column(db.String)
    createtime = db.Column(db.DateTime)
    reply = db.Column(db.String)
    replytime = db.Column(db.DateTime)

    def __init__(self, articleid, userid, content, ip):
        self.articleid = articleid
        self.userid = userid
        self.content = content
        self.ip = ip
        self.createtime = time.time()
