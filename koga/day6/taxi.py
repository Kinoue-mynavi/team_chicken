import sys
args=sys.argv
from math import ceil
#引数の格納
taxi_distance=int(args[1])
#初乗り距離・料金の設定
STARTING_DISTANCE=1500
STARTING_FARE=630
#初乗り以降の距離・料金の設定
CHARGE_OCCURENCE_DISTANCE=344
CHARGE_PER_DISTANCE=98

def fare_calculation(distance):
    """
    タクシーの運賃を計算する関数
    入力する値：距離(m)
    出力される値：値段(円)

    if文:初乗り距離以内かどうかの条件文
    """
    if distance<=STARTING_DISTANCE:
        fare_sum=STARTING_FARE
    else:
        distance_exclude_starting=distance-STARTING_DISTANCE
        charge_applying_distance=ceil(distance_exclude_starting/CHARGE_OCCURENCE_DISTANCE)
        fare_exclude_starting=charge_applying_distance*CHARGE_PER_DISTANCE
        fare_sum=STARTING_FARE+fare_exclude_starting
    return fare_sum

taxi_fare_sum=fare_calculation(taxi_distance)
print(taxi_fare_sum,end="")

