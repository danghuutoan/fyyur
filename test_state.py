from app import db, State, City
import pytz
from datetime import datetime

state = State.query.all()
print(state[0].city.name)
