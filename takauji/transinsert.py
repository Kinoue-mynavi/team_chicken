##呪文##
import sys
args = sys.argv

#データベースのインポート
from database import session
from tables import transport
from datetime import date
##--##

#引数を設定する
date = int(args[1])
seq = int(args[2])
departure = str(args[3])
arrival = str(args[4])
via = str(args[5])
amount = int(args[6])

date = date(int(dt[0:4]), int(dt[4:6]), int(dt[6:8]))
#引数に設定した値を追加

start_dis = session.query(.kilo).filter_by(name = start).first()