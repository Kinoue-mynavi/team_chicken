import sys
from tables import Stations
from database import session

first_arg = sys.argv[1]
second_arg = sys.argv[2]

# Fetch
def get_station(station_name):
    return session.query(Stations).filter_by(
        name=station_name
    ).first()

def calc_distance(station_name1, station_name2):
    if station_name1 and station_name2:
      first_kilo = get_station(station_name1).kilo
      second_kilo = get_station(station_name2).kilo

      return round(first_kilo - second_kilo, 2) if first_kilo > second_kilo else round(second_kilo - first_kilo, 2)
    else:
      return "Error: Please enter the first and second arguments"

# FIXME: エラーハンドリングを実装する
if __name__ == '__main__':
    print(calc_distance(first_arg, second_arg))