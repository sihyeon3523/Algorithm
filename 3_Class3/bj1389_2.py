# 3시 20분 ~

import sys
from collections import deque

n, m  = map(int, input().split()) # 유저의 수, 친구 관계의 수
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split()) # 친구 a, 친구 b
    # a = [b,c,d]
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    num = [0]*(n+1) # 단계 수 
    q = deque()
    visited[start] = 1 # 방문
    q.append(start)

    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                num[i] = num[a] + 1 # 단계수 더하기 
                q.append(i) 
                visited[i] = 1
    return sum(num)


result = []
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    result.append(bfs(graph, i))

print(result.index(min(result))+1)


''' 둘은 같다 [0, 0, 0, 0, 0]
print([0 for _ in range(5)])
print([0]*(5))
'''