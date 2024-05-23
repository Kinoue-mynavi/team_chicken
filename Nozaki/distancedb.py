from database import session
from tables import Stations

stations = session.query(Stations).all()

# 第1引数を取得
import sys
args = sys.argv

# 第2,3引数を取得
name1 = args[1]
name2 = args[2]

# SELECT（データ抽出）
station1 = session.query(Stations.kilo).filter_by(name = name1).first()
station2 = session.query(Stations.kilo).filter_by(name = name2).first()

distance = (station2.kilo - station1.kilo)
print("{:.2f}".format(distance))
