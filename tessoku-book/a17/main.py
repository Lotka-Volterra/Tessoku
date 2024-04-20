import copy
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# a,bのインデックスがai,biに対応するように調節
a = [0, 0] + a
b = [0, 0, 0] + b
dp = [0] * (n + 1)
sp=[[]for i in range(n+1)]
# dp[2]はdp[1]から1だけ移動するしかない
dp[2] = a[2]
sp[1]=[1]
sp[2]=[1,2]
# dp[3]以降は移動方法が2種類ある
for i in range(3, n + 1):
    ai = dp[i - 1] + a[i]
    bi = dp[i - 2] + b[i]
    # print(ai,bi)
    if min(ai,bi)==ai:
        dp[i]=ai
        spi=copy.copy(sp[i-1])
        spi.append(i)
        sp[i]=spi
    else:
        dp[i]=bi
        spi=copy.copy(sp[i-2])
        spi.append(i)
        sp[i]=spi
    # print(sp)
print(len(sp[n]))
print(*sp[n])
