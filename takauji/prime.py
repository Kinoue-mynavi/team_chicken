#呪文
import sys
args = sys.argv

#整数を入力
num = int(args[1])

#素数かどうか判定する関数
def prime_decision(num):
    for i in range(2,num):
        if num%i ==0:
            return str("not")
    return str("Prime")
        
#1000以上ならこの関数を使用しない
if num >=1000:
    print("1000以上は判定できません",end="")

else:
    a = prime_decision(num)
    print (a,end="")