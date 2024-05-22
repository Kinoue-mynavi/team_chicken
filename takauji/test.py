##--呪文--#
import sys
args = sys.argv
#四捨五入のモジュール

##----##

##--入力--##
#唐揚げ定食の数を入力
karaage = int(args[1])

#カレー定食の数を入力
curry = int(args[2])
##----##

#売上高の計算
karaage_sales = karaage*760
curry_sales = curry*850
sales = karaage_sales + curry_sales

#原価の計算
karaage_prime = karaage_sales*0.323
curry_prime = curry_sales*0.284
prime = karaage_prime + curry_prime

#粗利の計算
karaage_gross = karaage_sales - karaage_prime
curry_gross = curry_sales - curry_prime
gross = karaage_gross + curry_gross

#売上高、原価、粗利を出力
print(sales,prime,gross,end="")