from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL
from startup.db import db, app
from models.artist import Artist
from models.venue import Venue

states = [
    (1, 'AL'),
    (2, 'AK'),
    (3, 'AZ'),
    (4, 'AR'),
    (5, 'CA'),
    (6, 'CO'),
    (7, 'CT'),
    (8, 'DE'),
    (9, 'DC'),
    (10, 'FL'),
    (11, 'GA'),
    (12, 'HI'),
    (13, 'ID'),
    (14, 'IL'),
    (15, 'IN'),
    (16, 'IA'),
    (17, 'KS'),
    (18, 'KY'),
    (19, 'LA'),
    (20, 'ME'),
    (21, 'MT'),
    (22, 'NE'),
    (23, 'NV'),
    (24, 'NH'),
    (25, 'NJ'),
    (26, 'NM'),
    (27, 'NY'),
    (28, 'NC'),
    (29, 'ND'),
    (30, 'OH'),
    (31, 'OK'),
    (32, 'OR'),
    (33, 'MD'),
    (34, 'MA'),
    (35, 'MI'),
    (36, 'MN'),
    (37, 'MS'),
    (38, 'MO'),
    (39, 'PA'),
    (40, 'RI'),
    (41, 'SC'),
    (42, 'SD'),
    (43, 'TN'),
    (44, 'TX'),
    (45, 'UT'),
    (46, 'VT'),
    (47, 'VA'),
    (48, 'WA'),
    (49, 'WV'),
    (50, 'WI'),
    (51, 'WY'),
]


class ShowForm(FlaskForm):
    artist_choices = []
    venue_choices = []

    def __init__(self, artist_choices=[], venue_choices=[], **kwargs):
        super().__init__(**kwargs)
        self.artist_id.choices = artist_choices
        self.venue_id.choices = venue_choices

    # artist_choices = db.session.query(Artist.id, Artist.name).distinct().all()
    artist_id = SelectField('artist_id', choices=artist_choices)
    # venue_choices = db.session.query(Venue.id, Venue.name).distinct().all()
    venue_id = SelectField('veneu_id', choices=venue_choices)
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default=datetime.today()
    )


class VenueForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=states
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link', validators=[URL()]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=[
            (1, 'Alternative'),
            (2, 'Blues'),
            (3, 'Classical'),
            (4, 'Country'),
            (5, 'Electronic'),
            (6, 'Folk'),
            (7, 'Funk'),
            (8, 'Hip-Hop'),
            (9, 'Heavy Metal'),
            (10, 'Instrumental'),
            (11, 'Jazz'),
            (12, 'Musical Theatre'),
            (13, 'Pop'),
            (14, 'Punk'),
            (15, 'R&B'),
            (16, 'Reggae'),
            (17, 'Rock n Roll'),
            (18, 'Soul'),
            (19, 'Other'),
        ]
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(message='Must be a valid URL')]
    )


class ArtistForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=states)
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=[
            (1, 'Alternative'),
            (2, 'Blues'),
            (3, 'Classical'),
            (4, 'Country'),
            (5, 'Electronic'),
            (6, 'Folk'),
            (7, 'Funk'),
            (8, 'Hip-Hop'),
            (9, 'Heavy Metal'),
            (10, 'Instrumental'),
            (11, 'Jazz'),
            (12, 'Musical Theatre'),
            (13, 'Pop'),
            (14, 'Punk'),
            (15, 'R&B'),
            (16, 'Reggae'),
            (17, 'Rock n Roll'),
            (18, 'Soul'),
            (19, 'Other'),
        ]
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL(message='Must be a valid URL')]
    )

# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM
