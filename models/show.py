from startup.db import db


class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column('artist_id', db.Integer,
                          db.ForeignKey('artist.id'))
    venue_id = db.Column('venue_id', db.Integer,
                         db.ForeignKey('venue.id'))
    start_time = db.Column(db.DateTime(timezone=True))
