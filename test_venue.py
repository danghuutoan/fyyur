from app import db, Venue, Show
import pytz
from datetime import datetime
venue = Venue.query.get(1)
print(venue.state.name)
print(venue.state.city.name)
