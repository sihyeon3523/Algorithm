# 양방향 그래프
# 주변 사람들 & 최솟값 
# --> 그래프 

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    # 1 : [1,2,3] 2 : [1,4,5]
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    num = [0]*(n+1)
    q = deque()
    visited[start] = 1
    q.append(start)

    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                num[i] = num[a] + 1
                q.append(i)
                visited[i] = 1
    return sum(num)

result = []

for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    result.append(bfs(graph, i))

print(result.index(min(result))+1)