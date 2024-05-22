import sys
arg = sys.argv

karaage_order = int(arg[1])
carry_order = int(arg[2])

if 0 <= karaage_order <= 2000 and 0 <= carry_order <= 2000:
    sales = 760 * karaage_order + 850 * carry_order
else:
    pass

print(sales,end="")