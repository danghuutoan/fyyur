from app import db, Artist, Venue, Show, format_datetime
from datetime import datetime, timezone
import pytz


# artists = Artist.query.all()

# # artists = list(map(Artist.format, Artist.query.all()))
# for artist in artists:
#     print((artist.shows[0].venue.name))

# data = list(filter(lambda d: d.start_time >
#                    datetime.now().replace(tzinfo=pytz.utc), artists[2].shows))
# print(data)
# artist = Artist.query.get(1)
# artist.seeking_description = "Looking for shows to perform at in the San Francisco Bay Area!"

# # artist2 = Artist.query.get(2)
# # artist2.website = ["Jazz"]

# # artist3 = Artist.query.get(3)
# # artist3.website = ["Jazz", "Classical"]

# db.session.commit()
# db.session.close()

result = Venue.query.distinct(Venue.city)
print(result)
