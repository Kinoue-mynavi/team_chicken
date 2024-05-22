LAST_NAME_LIST = [
    "Kurita",
    "Tanaka",
    "Kaneda",
    "Noda",
    "Koyama",
    "Adachi",
    "Kuriyama",
    "Ohyama",
    "Kishida"
]

def is_odd(num):
    return num % 2 != 0

def pick():
    result_list = []
    for i in range(len(LAST_NAME_LIST)):
        if is_odd(i):
            result_list.append(LAST_NAME_LIST[i])
            
    return result_list

    
if __name__ == '__main__':
    print(pick())
