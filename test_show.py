from app import db, Show
import pytz

show = Show.query.get(1)

print(show.venue)
