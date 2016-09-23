from app import db  # NOQA


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    key = db.Column(db.String)
    description = db.Column(db.String)
    name_cn = db.Column(db.String)
    name_en = db.Column(db.String)

    def __init__(self, name, key, name_cn, name_en, description):
        self.name = name
        self.key = key
        self.name_cn = name_cn
        self.name_en = name_en
