import sys

args = sys.argv

input_number = int(args[1])

FIXED_FARE_DISTANCE = 1500
CHANGEABLE_FARE_DISTANCE = 344

FIXED_FARE = 630
CHANGEABLE_FARE = 98

def calc_fare(distance: int):
    fare = FIXED_FARE
    if (distance > 1500):
        additional_distance = distance - FIXED_FARE_DISTANCE
        distance_count = round(additional_distance / CHANGEABLE_FARE_DISTANCE)
        additional_fare = CHANGEABLE_FARE * distance_count if distance_count > 0 else CHANGEABLE_FARE
        fare = fare + additional_fare
    return fare
    
if __name__ == '__main__':
    print(calc_fare(input_number))
