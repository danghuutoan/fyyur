from app import db, Venue, Show
import pytz
from datetime import datetime
venue = Venue.query.get(3)
print(datetime.now())
print(venue.shows.filter(Show.start_time >=
                         datetime.now().replace(tzinfo=pytz.utc)).all())
