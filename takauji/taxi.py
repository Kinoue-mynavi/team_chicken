#呪文
import sys
args = sys.argv

#乗車距離を引数に入力
distance = int(args[1])

###--タクシーの距離の分岐--###
##初乗り1500mまでは630円
if distance <= 1500:
    fare = 630

##1500m以後の場合##
else:
    if (distance-1500) %344 == 0:
        a = (distance-1500)/344

    else:
        a = (distance-1500)/344 + 1
    
    fare = 630 + 98 * int(a)

print(fare,end="")
    