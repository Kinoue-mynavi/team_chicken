import sys
arg = sys.argv

from decimal import Decimal, ROUND_HALF_UP

karaage_order = int(arg[1])
carry_order = int(arg[2])

def calclunch(karaage_order,carry_order):

    karaage_sales = 760 * karaage_order
    carry_sales = 850 * carry_order

    karaage_cost = Decimal(0.323*(760 * karaage_order)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    carry_cost = Decimal(0.284*(850 * carry_order)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

    karaage_profit = karaage_sales - karaage_cost
    carry_profit = carry_sales - carry_cost
    
    sales = karaage_sales + carry_sales
    prime_cost = karaage_cost + carry_cost
    gross_profit = karaage_profit + carry_profit

    return sales , prime_cost ,gross_profit

if 0 <= karaage_order <= 2000 and 0 <= carry_order <= 2000:
    sales, prime_cost, gross_profit = calclunch(karaage_order,carry_order)
    print("売上：" + str(sales) + "、原価：" + str(prime_cost) + "、粗利：" + str(gross_profit),end="")
else:
    pass
