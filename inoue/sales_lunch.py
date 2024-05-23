import sys

args = sys.argv

input_number1 = int(args[1])
input_number2 = int(args[2])

FRIED_CHICKEN_PRICE = 760
CARREY_PRICE = 850

def calc_earnings(fried_chicken_order_count, carrey_order_count):
    return FRIED_CHICKEN_PRICE * fried_chicken_order_count + CARREY_PRICE * carrey_order_count
    
if __name__ == '__main__':
    print(calc_earnings(input_number1, input_number2))
