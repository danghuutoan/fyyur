from app import db, Artist, Venue, Show, format_datetime
from datetime import datetime, timezone
import pytz


venue1 = Venue()
venue1.name = "The Musical Hop"
venue1.genres = ["Jazz", "Reggae", "Swing", "Classical", "Folk"]
venue1.address = "1015 Folsom Street"
venue1.city = "San Francisco"
venue1.state = "CA"
venue1.phone = "123-123-1234"
venue1.website = "https://www.themusicalhop.com"
venue1.facebook_link = "https://www.facebook.com/TheMusicalHop"
venue1.seeking_talent = True
venue1.seeking_description = "We are on the lookout for a local artist to play every two weeks. Please call us."
venue1.image_link = "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
db.session.add(venue1)

venue2 = Venue()
venue2.name = "The Dueling Pianos Bar"
venue2.genres = ["Classical", "R&B", "Hip-Hop"]
venue2.address = "335 Delancey Street"
venue2.city = "New York"
venue2.state = "NY"
venue2.phone = "914-003-1132"
venue2.website = "https://www.theduelingpianos.com"
venue2.facebook_link = "https://www.facebook.com/theduelingpianos"
venue2.seeking_talent = False
venue2.image_link = "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"
db.session.add(venue2)

venue3 = Venue()
venue3.name = "Park Square Live Music & Coffee"
venue3.genres = ["Rock n Roll", "Jazz", "Classical", "Folk"]
venue3.address = "34 Whiskey Moore Ave"
venue3.city = "San Francisco"
venue3.state = "CA"
venue3.phone = "415-000-1234"
venue3.website = "https://www.parksquarelivemusicandcoffee.com"
venue3.facebook_link = "https://www.facebook.com/ParkSquareLiveMusicAndCoffee"
venue3.seeking_talent = False
venue3.image_link = "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"
db.session.add(venue3)

db.session.commit()
db.session.close()
