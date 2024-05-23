import sys
args=sys.argv

#商品の辞書型の設定
menu_pricing_table={"唐揚げ定食":760,"カレーセット":850}
cost_table={"唐揚げ定食":0.323,"カレーセット":0.284}

#引数を変数に格納
karaage_order_number=int(args[1])
curry_order_number=int(args[2])

def profitcalc(karaage,curry):
    """
    注文数から売り上げ、原価、粗利を算出する関数
    入力する値：各メニューの注文数
    出力する値：全メニューの合計売上、原価、粗利
    """
    #注文数に対して売り上げを算出
    sales_karaage=karaage*menu_pricing_table["唐揚げ定食"]
    sales_curry=curry*menu_pricing_table["カレーセット"]
    #合計を算出
    sales_sum=sales_karaage+sales_curry
    #各売り上げに対して原価を算出
    cost_karaage=round(sales_karaage*cost_table["唐揚げ定食"])
    cost_curry=round(sales_curry*cost_table["カレーセット"])
    #合計を算出
    cost_sum=cost_karaage+cost_curry
    #売り上げと原価を用いて粗利を算出
    gross_profit_karaage=sales_karaage-cost_karaage
    gross_profit_curry=sales_curry-cost_curry
    #合計を算出
    gross_profit_sum=gross_profit_karaage+gross_profit_curry
    #結果の出力
    print("売上高：{0}、原価：{1}、粗利：{2}".format(sales_sum,cost_sum,gross_profit_sum),end="")

profitcalc(karaage_order_number,curry_order_number)