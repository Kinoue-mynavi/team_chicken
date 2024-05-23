#呪文
import sys
args = sys.argv

from database import session
from tables import stations


#入力
start = str (args[1])
goal = str (args[2])

#データを抽出
start_dis = session.query(stations.kilo).filter_by(name = start).first()
goal_dis = session.query(stations.kilo).filter_by(name = goal).first()

#距離の計算
distance = (round (abs(start_dis.kilo - goal_dis.kilo),2))

#出力
print(distance,end="")