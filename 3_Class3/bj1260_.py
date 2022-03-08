# 4시 29분 ~

# DFS --> 재귀 : 같은 방향으로 계속 탐색
# BFS --> 테큐(우선순위 큐) : 사방으로 퍼지며 동시에 탐색
from collections import deque
import sys
read = sys.stdin.readline

n, m, v = map(int, input().split()) # 정점의 개수, 간선의 개수, 탐색 시작점

graph = [[0]*1001 for _ in range(1001)]
visit_bfs = [0]*(n+1)
visit_dfs = [0]*(n+1)

# graph[행][열] --> 연결된 정점 표시 
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    visit_dfs[v] = 1
    print(v, end = " ")
    for i in range(1, n+1):
        if visit_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visit_bfs[v] = 1
    
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n+1):
            if visit_bfs[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_bfs[i] = 1

dfs(v)
print()
bfs(v)