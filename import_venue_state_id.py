from app import db, Venue, Show


venue1 = Venue.query.get(1)
venue1.state_id = 1

venue3 = Venue.query.get(3)
venue3.state_id = 1

venue2 = Venue.query.get(2)
venue2.state_id = 2


db.session.commit()
