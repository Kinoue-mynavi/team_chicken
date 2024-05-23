from database import session
from tables import Stations2

stations2=Stations2(
        seq=1,
        name="東京",
        kilo=0.00
    )

stations2=Stations2(
        seq=2,
        name="品川",
        kilo=6.78
    )
stations2=Stations2(
        seq=3,
        name="新横浜",
        kilo=25.54
    )
stations2=Stations2(
        seq=4,
        name="名古屋",
        kilo=342.02
    )
stations2=Stations2(
        seq=5,
        name="京都",
        kilo=476.31
    )
stations2=Stations2(
        seq=6,
        name="新大阪",
        kilo=515.35
    )


session.add(stations2)

session.commit()

v=session.query(Stations2).all()

for item in v:
    print(item.name)