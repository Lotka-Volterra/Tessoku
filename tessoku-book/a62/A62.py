import sys
# from functools import lru_cache

# !!!!PyPyは再帰関数の実行速度が遅いことがあり、Python3でまず試してみる!!!!
# 再帰呼び出しの深さの上限を 10**6 に設定、設定を上げておかないと途中で再帰呼び出しを切り上げてREになる
sys.setrecursionlimit(10**6)


# 深さ優先探索の再帰関数
# メモ化再帰　再帰関数の呼び出し時に、同じ引数の再帰関数が呼ばれる場合に備えて計算結果をメモしておく、Windowsでは落ちるので使わない
# @lru_cache
def DeepFirtstSearch(position, adjacencyList, visitedList):
    # 今訪れた頂点をTrueに
    visitedList[position] = True
    # print(position,len(adjacencyList[position]))
    for i in adjacencyList[position]:
        # 隣接した頂点が未踏の場合、その頂点へ行く（再帰）
        if visitedList[i] == False:
            DeepFirtstSearch(i, adjacencyList, visitedList)
    # 一つ前の頂点に戻る
    return None


n, m = map(int, input().split())
# 頂点n個＋1個の要素をもつFalseのリストを作る。訪れた場合、要素をTrueにする。
visited = [False] * (n + 1)
# 頂点0は存在しないが、0-indexedに合わせるため作成している。Trueにしておく
visited[0] = True
# 隣接行列。頂点0から頂点nまで合計n+1のリストに、各頂点iと隣接する頂点のリストを作成
adjacencyList = [[] for i in range(n + 1)]
# print(len(adjacencyList))
for i in range(m):
    a, b = map(int, input().split())
    adjacencyList[a].append(b)
    adjacencyList[b].append(a)
DeepFirtstSearch(1, adjacencyList, visited)

# 1からnまで、全ての頂点を訪れたか調べる。全ての頂点を訪れられた＝連結
for i in range(1, n + 1):
    if visited[i] == False:
        print("The graph is not connected.")
        quit()
print("The graph is connected.")
