from database import session
from tables import Stations

stations = session.query(Stations).all()

for item in stations:
    print(item.seq, item.name, item.kilo)

