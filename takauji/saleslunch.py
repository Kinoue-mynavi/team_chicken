#呪文
import sys
args = sys.argv

##--入力--##
#唐揚げ定食の数を入力
karaage = int(args[1])

#カレー定食の数を入力
curry = int(args[2])
##----##

#売上高の計算
sales = karaage*760 + curry*850

#売上高を出力
print(sales,end="")