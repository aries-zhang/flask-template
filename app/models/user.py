from app import db  # NOQA


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uniqueid = db.Column(db.String)
    name = db.Column(db.String)
    source = db.Column(db.Integer)
    location = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    domain = db.Column(db.String)
    portrait = db.Column(db.String)
    gender = db.Column(db.Integer)
    verified = db.Column(db.Boolean)
    createtime = db.Column(db.DateTime)

    def __init__(self, uniqueid, name, source, portrait, gender):
        self.name = name
        self.uniqueid = uniqueid
        self.source = source
        self.portrait = portrait
        self.gender = gender
