from startup.db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


venue_genres = db.Table('venue_genres',
                        db.Column('genre_id', db.Integer,
                                  db.ForeignKey('genre.id')),
                        db.Column('venue_id', db.Integer,
                                  db.ForeignKey('venue.id'))
                        )

artist_genres = db.Table('artist_genres',
                         db.Column('genre_id', db.Integer,
                                   db.ForeignKey('genre.id')),
                         db.Column('artist_id', db.Integer,
                                   db.ForeignKey('artist.id'))
                         )
