from app import db, Genre
from datetime import datetime, timezone
import pytz
["Jazz", "Reggae", "Swing", "Classical", "Folk"]
genre1 = Genre(name="Jazz")
genre2 = Genre(name="Reggae")
genre3 = Genre(name="Swing")
genre4 = Genre(name="Classical")
genre5 = Genre(name="Folk")
genre6 = Genre(name="R&B")
genre7 = Genre(name="Hip-Hop")
genre8 = Genre(name="Rock n Roll")

db.session.add(genre1)
db.session.add(genre2)
db.session.add(genre3)
db.session.add(genre4)
db.session.add(genre5)
db.session.add(genre6)
db.session.add(genre7)
db.session.add(genre8)

db.session.commit()
db.session.close()
