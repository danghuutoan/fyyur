from startup.db import db

from models.genre import venue_genres


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(500), nullable=True)
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500), nullable=True)
    shows = db.relationship('Show', backref=db.backref('venue', lazy='joined'))
    genres = db.relationship(
        'Genre', secondary=venue_genres, backref=db.backref('venues', lazy='dynamic'))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
