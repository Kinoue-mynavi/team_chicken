import sys
arg = sys.argv

number = int(arg[1])

def prime(n):
    for i in range(2,n,1):
        if n % i == 0:
            return str("not")
    return str("Prime")

if number < 1000:
    result = prime(number)
    print(result,end="")
else:
    print("1000以上は判定できません",end="")
