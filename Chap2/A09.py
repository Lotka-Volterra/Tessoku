# H行W列の行列に二次元配列を格納。
# H回の配列の入力をXに格納。
H, W, N = map(int, input().split())

# 配列 Z は二次元累積和計算用の、H+1行 W+1列の二次元配列。行、列を1つ多くとることで、境界を気にせず二次元累積和を計算できる。
Z = [[0] * (W + 2) for i in range(H + 2)]
for i in range(N):
    A, B, C, D = map(int, input().split())
    # 配列 Z は既に初期化済み
    # AからC行の、B列からC列まで、横方向に前日差を設定。
    for h in range(A,C+1):
        Z[h][B]+=1
        Z[h][D+1]-=1
# 横方向に累積和をとる
for h in range(1, H+1):
	for w in range(1, W+1):
		Z[h][w] = Z[h][w-1] + Z[h][w]

# 配列 Z の[i][j]要素は、H行W列の配列の[i-i][j-1]要素に相当。
TwoDimensionalSum=[Z[i][1:W+1] for i in range(1,H+1)]

for i in range(H):
    print(*TwoDimensionalSum[i])
