n= int(input())

answer = ''
for i in range(1,11):
    sho = n//2**(10-i)
    n = n%2**(10-i)
    answer+=str(sho)
print(answer)