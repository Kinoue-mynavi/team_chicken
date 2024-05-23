import sys

args = sys.argv

input_number = int(args[1])

if __name__ == '__main__':
    print(f"{input_number} {abs(input_number)}")