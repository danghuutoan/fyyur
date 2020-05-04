from app import db, Artist, State

artist1 = Artist.query.get(1)
artist1.state_id = 1

artist2 = Artist.query.get(2)
artist2.state_id = 2
artist3 = Artist.query.get(3)
artist3.state_id = 1
db.session.add(artist1)
db.session.add(artist2)
db.session.add(artist3)

db.session.commit()
