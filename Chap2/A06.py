n, q = map(int, input().split())
a = list(map(int, input().split()))
visitorsum = [0]*(n+1)
kokomadenosum = 0
for i in range(n):
    kokomadenosum += a[i]
    visitorsum[i+1] = kokomadenosum

for i in range(q):
    l, r = map(int, input().split())
    print(visitorsum[r]-visitorsum[l-1])
