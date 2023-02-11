n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if 1 <= k-(i+j) <= n:
            count += 1
print(count)
