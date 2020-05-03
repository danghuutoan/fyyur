from app import db, Artist, Venue, Show, format_datetime
from datetime import datetime, timezone
import pytz

#  data1 = {
#         "id": 4,
#         "name": "Guns N Petals",
#         "genres": ["Rock n Roll"],
#         "city": "San Francisco",
#         "state": "CA",
#         "phone": "326-123-5000",
#         "website": "https://www.gunsnpetalsband.com",
#         "facebook_link": "https://www.facebook.com/GunsNPetals",
#         "seeking_venue": True,
#         "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
#         "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
#         "past_shows": [{
#             "venue_id": 1,
#             "venue_name": "The Musical Hop",
#             "venue_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
#             "start_time": "2019-05-21T21:30:00.000Z"
#         }],
#         "upcoming_shows": [],
#         "past_shows_count": 1,
#         "upcoming_shows_count": 0,
#     }
#     data2 = {
#         "id": 5,
#         "name": "Matt Quevedo",
#         "genres": ["Jazz"],
#         "city": "New York",
#         "state": "NY",
#         "phone": "300-400-5000",
#         "facebook_link": "https://www.facebook.com/mattquevedo923251523",
#         "seeking_venue": False,
#         "image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
#         "past_shows": [{
#             "venue_id": 3,
#             "venue_name": "Park Square Live Music & Coffee",
#             "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
#             "start_time": "2019-06-15T23:00:00.000Z"
#         }],
#         "upcoming_shows": [],
#         "past_shows_count": 1,
#         "upcoming_shows_count": 0,
#     }
#     data3 = {
#         "id": 6,
#         "name": "The Wild Sax Band",
#         "genres": ["Jazz", "Classical"],
#         "city": "San Francisco",
#         "state": "CA",
#         "phone": "432-325-5432",
#         "seeking_venue": False,
#         "image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
#         "past_shows": [],
#         "upcoming_shows": [{
#             "venue_id": 3,
#             "venue_name": "Park Square Live Music & Coffee",
#             "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
#             "start_time": "2035-04-01T20:00:00.000Z"
#         }, {
#             "venue_id": 3,
#             "venue_name": "Park Square Live Music & Coffee",
#             "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
#             "start_time": "2035-04-08T20:00:00.000Z"
#         }, {
#             "venue_id": 3,
#             "venue_name": "Park Square Live Music & Coffee",
#             "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
#             "start_time": "2035-04-15T20:00:00.000Z"
#         }],
#         "past_shows_count": 0,
#         "upcoming_shows_count": 3,
#     }
artist1 = Artist()
artist1.name = "Guns N Petals"
artist1.genres = ["Rock n Roll"]
artist1.city = "San Francisco"
artist1.state = "CA"
artist1.phone = "326-123-5000"
artist1.website = "https://www.gunsnpetalsband.com"
artist1.facebook_link = "https://www.facebook.com/GunsNPetals"
artist1.seeking_venue = True
artist1.seeking_description = "Looking for shows to perform at in the San Francisco Bay Area!"
artist1.image_link = "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
db.session.add(artist1)

artist2 = Artist()
artist2.name = "Matt Quevedo"
artist2.genres = ["Jazz"]
artist2.city = "New York"
artist2.state = "NY"
artist2.phone = "300-400-5000"
artist2.facebook_link = "https://www.facebook.com/mattquevedo923251523"
artist2.seeking_venue = False
artist2.image_link = "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80"
db.session.add(artist2)

artist3 = Artist()
artist3.name = "The Wild Sax Band"
artist3.genres = ["Jazz", "Classical"]
artist3.city = "San Francisco"
artist3.state = "CA"
artist3.phone = "432-325-5432"
artist3.seeking_venue = False
artist3.image_link = "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80"
db.session.add(artist3)

db.session.commit()
db.session.close()
