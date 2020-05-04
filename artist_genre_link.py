from app import db, Genre, Artist
import pytz

Jazz = Genre.query.get(1)
Reggae = Genre.query.get(2)
Swing = Genre.query.get(3)
Classical = Genre.query.get(4)
Folk = Genre.query.get(5)
R_n_B = Genre.query.get(6)
Hip_Hop = Genre.query.get(7)
Rock_n_Roll = Genre.query.get(8)


artist1 = Artist.query.get(1)
artist1.genres.append(Jazz)
artist1.genres.append(Reggae)
artist1.genres.append(Swing)
artist1.genres.append(Classical)
artist1.genres.append(Folk)


artist2 = Artist.query.get(2)
artist2.genres.append(Classical)
artist2.genres.append(R_n_B)
artist2.genres.append(Hip_Hop)


artist3 = Artist.query.get(3)
artist3.genres.append(Rock_n_Roll)
artist3.genres.append(Jazz)
artist3.genres.append(Classical)
artist3.genres.append(Folk)

db.session.add(artist1)
db.session.add(artist2)
db.session.add(artist3)
db.session.commit()
db.session.close()
