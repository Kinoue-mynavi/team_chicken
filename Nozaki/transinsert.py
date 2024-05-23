from database import session
from tables import transport
from datetime import date

import sys
args = sys.argv

use_date = args[1] # 利用日
sequence = int(args[2])  # 連番
departure_place = args[3]  # 出発地
arrival_place = args[4]  # 到着地
transportation_facilities = args[5]  # 利用交通機関
price = int(args[6])  # 金額

datetime = date(int(use_date[:4]),int(use_date[4:6]),int(use_date[6:8]))

#登録したデータ
koutuuhi_1 =session.query(transport).filter_by(date=datetime).first()
koutuuhi_2=session.query(transport).filter_by(seq=sequence).first()



new_transport= transport(
    date= datetime,
    seq=sequence,
    departure=departure_place,
    arrival=arrival_place,
    via=transportation_facilities,
    amount=price
    )

session.add(new_transport)
session.commit()

# print(koutuuhi_1)

if koutuuhi_1 is None and koutuuhi_2 is None:
    session.add(new_transport)
    session.commit()
    print("交通費精算テーブルにデータを登録しました。")
else:
    print("交通費清算テーブルにデータを登録できませんでした")


