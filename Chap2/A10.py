n = int(input())
a = list(map(int, input().split()))
d = int(input())
l = [0]*d
r = [0]*d
for i in range(d):
    li, ri = map(int, input().split())
    # 格納時に部屋番号を-1して０indexedにする
    l[i] = li-1
    r[i] = ri-1
maxl = a[0]
p = [0]*n
for i in range(n):
    maxl = max(maxl, a[i])
    p[i] = maxl
q = [0]*n
maxr = a[n-1]
for i in range(n-1, -1, -1):
    maxr = max(maxr, a[i])
    q[i] = maxr

for i in range(d):
    print(max(p[l[i]-1], q[r[i]+1]))
