#呪文
import sys
args = sys.argv

list = ["Kurita","Tanaka","Kaneda","Noda","Koyama","Adachi","Kuriyama","Ohyama","Kishida"]
odd_list = []

for i in range(1,len(list),2):
    odd_list.append(list[i])

print(odd_list,end="")
