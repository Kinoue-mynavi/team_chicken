import sys

args = sys.argv

input_number1 = int(args[1])
input_number2 = int(args[2])

FRIED_CHICKEN_PRICE = 760
CARREY_PRICE = 850

def calc_gross_profit(fried_chicken_order_count, carrey_order_count):
    # 売り上げ
    fried_chicken_sales = FRIED_CHICKEN_PRICE * fried_chicken_order_count
    carrey_sales = CARREY_PRICE * carrey_order_count
    total_sales = fried_chicken_sales + carrey_sales

    # 原価
    fried_chicken_cost_price = round(fried_chicken_sales * 0.323)
    carrey_cost_price = round(carrey_sales * 0.284)
    total_cost_price = fried_chicken_cost_price + carrey_cost_price

    # 粗利
    fried_chicken_gross_profit = fried_chicken_sales - fried_chicken_cost_price
    carrey_gross_profit = carrey_sales - carrey_cost_price
    total_gross_profit = fried_chicken_gross_profit + carrey_gross_profit

    return f"売上高：{total_sales}、原価：{total_cost_price}、粗利：{total_gross_profit}"

    
if __name__ == '__main__':
    print(calc_gross_profit(input_number1, input_number2))
