h,w= map(int,input().split())
hw=[]
hw.append([0]*(w+1))
for i in range(h):
    x= list(map(int,input().split()))
    for j in range(1,w):
        x[j]=x[j-1]+x[j]
    x=[0]+x
    hw.append(x)

tdhw=hw.copy()

for i in range(h+1):
    for j in range(w+1):
        tdhw[i][j]=tdhw[i-1][j]+tdhw[i][j]
q= int(input())

for i in range(q):
    a,b,c,d= map(int,input().split())
    print(tdhw[c][d]-(tdhw[a-1][d]+tdhw[c][b-1])+tdhw[a-1][b-1])
