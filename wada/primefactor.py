import sys
arg = sys.argv

number = int(arg[1])
primelist = []

def prime(n):
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            primelist.append(i)
    if n > 1:
        primelist.append(n)



prime(number)
print(primelist)


