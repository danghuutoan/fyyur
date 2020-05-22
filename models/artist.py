from startup.db import db
from models.genre import artist_genres


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    phone = db.Column(db.String(120))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500), nullable=True)
    website = db.Column(db.String(500), nullable=True)
    genres = db.relationship(
        'Genre', secondary=artist_genres, backref=db.backref('artists', lazy='dynamic'))
    shows = db.relationship(
        'Show', backref=db.backref('artist', lazy='select'))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
