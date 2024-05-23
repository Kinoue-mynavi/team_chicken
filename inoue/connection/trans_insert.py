import sys
from database import session
import datetime
from tables import Transport

args = sys.argv

input_date = str(args[1])
input_year = int(input_date[0:4])
input_month = int(input_date[4:6])
input_day = int(input_date[6:])

input_seq = int(args[2])
input_departure = str(args[3])
input_arrival = str(args[4])
input_via = str(args[5])
input_amount = int(args[6])

def add_transport(d, seq, departure, arrival, via, amount):
    station = Transport(
        date = d,
        seq = seq,
        departure = departure,
        arrival = arrival,
        via = via,
        amount = amount
    )
    session.add(station)
    session.commit()


if __name__ == '__main__':
    try:
        result = add_transport(
            datetime.date(input_year, input_month, input_day),
            input_seq,
            input_departure,
            input_arrival,
            input_via,
            input_amount
        )
        print("交通費精算テーブルにデータを登録しました")
    except:
        print("error:交通費精算テーブルにデータを登録できませんでした")
