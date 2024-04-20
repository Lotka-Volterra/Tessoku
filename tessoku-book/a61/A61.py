n, m = map(int, input().split())
adjacencyList = [[] for i in range(n + 1)]

for i in range(1, m + 1):
    a, b = map(int, input().split())
    adjacencyList[a].append(b)
    adjacencyList[b].append(a)
# print(*adjacencyList[1],sep=', ')
# print(type(adjacencyList[1]))
# print(type(*adjacencyList[1],sep=', '))
for i in range(1, n + 1):
    strList = str(", ".join(map(str, adjacencyList[i])))
    # print(type(strList))
    print(f"{i}: {{{strList}}}")
    # print(str(i) + ": {" + {0} + "}".format(strList))
    # print(": {" + {s} + "}".format(s=strList))
