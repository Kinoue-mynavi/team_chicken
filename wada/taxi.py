import sys
arg = sys.argv

distance = int(arg[1])

def calcfare(distance):
    if distance <= 1500:
        fare = 630
    elif (distance - 1500)%344 == 0:
        fare = 630 + 98 * int(distance-1500)/344 
    else:
        fare = 630 + 98 + 98 * int((distance-1500)/344)
    return round(fare)

print(calcfare(int(arg[1])),end="")