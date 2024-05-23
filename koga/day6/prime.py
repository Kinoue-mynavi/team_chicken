import sys
args=sys.argv
from math import floor
"""
ある数の約数となる素数はある数の平方根より小さいという性質を利用する。
入力値：任意の整数
出力：「not」(素数でない場合)「Prime」(素数の場合)
"""

#任意の数(1000未満)を入力
Number=int(args[1])
#任意の数の平方根を算出
square_root=Number**0.5
#平方根を整数値に近似する
square_root_approximation=floor(square_root)
#約数となりうる値を設定(最小値2)
PRIME_NUMBER=2

#任意の数が1000より小さいか判定
if Number<1000:
    #約数候補が平方根に到達するまで判定を行う。    
    while (PRIME_NUMBER<=square_root_approximation):
        #約数候補で任意の数を割り切ることができたら「not」と表示してループを終了
        if Number%PRIME_NUMBER==0:
            print("not",end="")
            break
        #約数候補で任意の数を割り切ることができなかったら約数候補に+1してもう一度判定を行う。「not」と表示してループを終了
        else:
            PRIME_NUMBER+=1
            #約数候補が平方根に到達したら「Prime」と表示(whileの条件文によってこの後ループが終了する)
            if(PRIME_NUMBER==square_root_approximation):
                print("Prime",end="")
else:
    print("1000以上は判定できません",end="")
    
    