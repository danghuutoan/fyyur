from app import db, Genre, Artist
import pytz

artist1 = Artist.query.get(1)

print(artist1.genres.all()[0].name)
# for genre in artist1.genres:
#     print(genre.name)
