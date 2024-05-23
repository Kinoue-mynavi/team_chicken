# 第１引数を取得
import sys
import math
args = sys.argv

# 基本運賃
Fare = int(630)

# 追加運賃
additional = int(98) 

# 第２引数を取得
distance = int(args[1])

# 距離が1500m以下の場合
if distance <= 1500:
     print(Fare)
else:
    distance -= int(1500)
    sum = Fare + additional * math.ceil(distance/344)
    print(sum)