import sys
args=sys.argv

#商品と価格の情報を辞書型に設定
menu_pricing_table={"唐揚げ定食":760,"カレーセット":850}
#引数を変数に格納
karaage_order_number=int(args[1])
curry_order_number=int(args[2])
#該当する商品の価格を算出
sales=karaage_order_number*menu_pricing_table["唐揚げ定食"]+curry_order_number*menu_pricing_table["カレーセット"]
#価格を出力
print(sales,end="")
