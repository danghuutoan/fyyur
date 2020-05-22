from startup.db import db


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))
    venues = db.relationship('Venue', backref='city', lazy=True)
    artists = db.relationship('Artist', backref='city', lazy=True)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
