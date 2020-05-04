from app import db, State, City
import pytz
from datetime import datetime

san_francisco = City(name='San Francisco')
new_york = City(name='New York')

CA = State(name='CA', city=san_francisco)
NY = State(name='NY', city=new_york)

db.session.add(CA)
db.session.add(NY)
db.session.commit()
