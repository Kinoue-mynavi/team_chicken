from database import session
from tables import Stations

stations=[
    Stations(
        seq=1,
        name="東京",
        kilo=0.00
    ),
    Stations(
        seq=2,
        name="品川",
        kilo=6.78
    ),
    Stations(
        seq=3,
        name="新横浜",
        kilo=25.54
    ),  
    Stations(
        seq=4,
        name="名古屋",
        kilo=342.02
    ),
    Stations(
        seq=5,
        name="京都",
        kilo=476.31
    ),
    Stations(
        seq=6,
        name="新大阪",
        kilo=515.35
    )
]

session.add(stations)

session.commit()

v=session.query(Stations).all()

for item in v:
    print(item.name)