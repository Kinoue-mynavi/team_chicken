namelist = [
    "Kurita", 
    "Tanaka", 
    "Kaneda", 
    "Noda", 
    "Koyama", 
    "Adachi", 
    "Kuriyama", 
    "Ohyama", 
    "Kishida"]

oddlist = []

for i in range(1,len(namelist),2):
    oddlist.append(namelist[i])

print(oddlist,end="")