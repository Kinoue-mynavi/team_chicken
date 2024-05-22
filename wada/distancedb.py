from database import session
from tables import stations

import sys
arg = sys.argv

departure = arg[1]
arrival = arg[2]

departure = session.query(stations.kilo).filter_by(name = departure).first()
arrival = session.query(stations.kilo).filter_by(name = arrival).first()

distance = departure.kilo - arrival.kilo

print(round(abs(departure.kilo - arrival.kilo),2))
