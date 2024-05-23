# 第1引数を取得
import sys
args = sys.argv

# 第2引数を取得
integer = int(args[1])

# 実行エラー
if integer < 1000:
    if integer <= 1:
        print("not")
    else:
        for i in range (2,int(integer**0.5)+1):
            if integer % i == 0:
             print("not")
             break
        else:
         print("Prime")
else:
    print("1000以上は判定できません")
