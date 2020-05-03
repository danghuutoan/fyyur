from app import db, Artist, Venue, Show, format_datetime
from datetime import datetime, timezone
import pytz

show1 = Show()
show1.venue_id = 1
show1.artist_id = 1
show1.artist_image_link = "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
show1.start_time = format_datetime("2019-05-21T21:30:00.000Z")
db.session.add(show1)

show2 = Show()
show2.venue_id = 3
show2.artist_id = 2
show2.artist_image_link = "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80"
show2.start_time = format_datetime(
    "2019-06-15T23:00:00.000Z")
db.session.add(show2)

show3 = Show()
show3.venue_id = 3
show3.artist_id = 3
show3.artist_image_link = "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80"
show3.start_time = format_datetime(
    "2035-04-01T20:00:00.000Z")
db.session.add(show3)

show4 = Show()
show4.venue_id = 3
show4.artist_id = 3
show4.artist_image_link = "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80"
show4.start_time = format_datetime(
    "2035-04-08T20:00:00.000Z")
db.session.add(show4)

show5 = Show()
show5.venue_id = 3
show5.artist_id = 3
show5.artist_image_link = "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80"
show5.start_time = format_datetime(
    "2035-04-15T20:00:00.000Z")
db.session.add(show5)

db.session.commit()
db.session.close()
