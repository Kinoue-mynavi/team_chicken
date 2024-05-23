# 第1引数を取得
import sys
args = sys.argv

# 第2,3引数を取得
Count1 = int(args[1])
Count2 = int(args[2])

# 値段
fri = int(760)
cury = int(850)

# 売り上げ
sum = ((fri * Count1) + (cury * Count2))
print(sum)


