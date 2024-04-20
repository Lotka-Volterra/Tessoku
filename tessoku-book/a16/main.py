n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# a,bのインデックスがai,biに対応するように調節
a = [0, 0] + a
b = [0, 0, 0] + b
dp = [0] * (n + 1)
# dp[2]はdp[1]から1だけ移動するしかない
dp[2] = a[2]
# dp[3]以降は移動方法が2種類ある
for i in range(3, n + 1):
    ai = dp[i - 1] + a[i]
    bi = dp[i - 2] + b[i]
    dp[i] = min(ai, bi)
print(dp[n])
