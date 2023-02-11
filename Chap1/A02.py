n, x = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
print('Yes') if x in a else print('No')
