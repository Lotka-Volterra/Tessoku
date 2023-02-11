#自分で書いたもの、多分while Trueの直下で正確に半分に分けられておらず、微妙に探索範囲が広まる場合があり、TLE連発
n, x = map(int, input().split())
a = list(map(int, input().split()))
startindex = 0
endindex = n-1
while True:
    midindex = (endindex-startindex+1)//2
    modifiedmidindex=startindex+midindex
    midA = a[modifiedmidindex-1]
    if x == midA:
        print(modifiedmidindex)
        quit()
    elif x < midA:
        endindex = modifiedmidindex-2
    else:
        startindex = modifiedmidindex

#本の記載を参考に修正したもの
n, x = map(int, input().split())
a = list(map(int, input().split()))
startindex = 0
endindex = n-1
while startindex<=endindex:
    midindex = (endindex+startindex)//2
    midA = a[midindex]
    if x == midA:
        print(midindex+1)
        quit()
    elif x < midA:
        endindex = midindex-1
    else:
        startindex = midindex+1
