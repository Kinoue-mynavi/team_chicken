import sys

args = sys.argv

input_number = int(args[1])

def is_prime(num):
    if num == 1:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def judge_prime(num):
    if (num >= 1000): return "1000以上は判定できません"
    return "Prime" if is_prime(num) else "not"


if __name__ == '__main__':
    print(f"{judge_prime(input_number)}")