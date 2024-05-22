from database import session
from tables import transport

from datetime import date

import sys
arg = sys.argv

dt = arg[1]
seq = int(arg[2])
departure = arg[3]
arrival = arg[4]
via = arg[5]
amount = int(arg[6])

dt = date(int(dt[0:4]), int(dt[4:6]), int(dt[6:8]))

count_date = session.query(transport.date).filter_by(date = dt).count()
count_seq = session.query(transport.seq).filter_by(seq = seq).count()

if count_date > 0 and count_seq > 0:
    print("error:交通費精算テーブルにデータを登録できませんでした")

else:
    port = transport(
        date=dt,
        seq=seq,
        departure=departure,
        arrival=arrival,
        via=via,
        amount=amount
        )

session.add(port)

session.commit()