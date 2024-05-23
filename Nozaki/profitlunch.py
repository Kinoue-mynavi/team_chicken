# 第1引数の取得
import sys
args = sys.argv

# 第2引数の取得
Count1 = int(args[1])
Count2 = int(args[2])

# 値段
fri = int(760)
cury = int(850)

# 売り上げの算出
sum1 = ((fri * Count1) + (cury * Count2))

# 原価の算出
fri_cost = (fri * 0.323)
cury_cost = (cury * 0.284)
sum2 = round((fri_cost * Count1) + (cury_cost * Count2))

# 粗利の算出
profit = sum1 - int(sum2)

# 出力
print(f"売上高：{sum1}、原価：{sum2}、粗利：{profit}" )

