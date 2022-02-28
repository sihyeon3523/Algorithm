# 간선 양방향 
# S2
# DFS와 BFS
# 12시 35분 ~

'''
 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
 더 이상 방문할 수 있는 점이 없는 경우 종료
 V부터 방문된 점을 순서대로 출력
 연결된 정점을 한 리스트로 넣어준 경우 --> 위, 아래, 오른쪽, 왼쪽 이동 필요 X
'''
# m이 최대 10,000개로 많이 받을 수 있기 때문에 시간 단축 필요
import sys
input = sys.stdin.readline 

# BFS --> While문 & 덱 
from collections import deque

# DFS --> 재귀
def dfs(v):
    # 방문 기록 & 방문한 정점 출력 
    visited_dfs[v] = 1
    print(v, end = " ")

    # 정점을 1부터 시작한다 즉, 정점 번호가 작은 것을 먼저 방문 
    for i in range(1, n+1):
        if visited_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited_bfs[v] = 1
    
    while q:
        # 접하는 정점의 가장 작은 것부터 탐색 
        v = q.popleft() 
        print(v, end = " ")

        # 정점이 가장 작은 것부터 탐색
        for i in range(1, n+1):
            if visited_bfs[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited_bfs[i] = 1


# 정점의 개수, 간선의 개수, 시작점
n, m, v = map(int, input().split()) 

# 정점은 1부터 시작하므로, n+1 만큼 리스트 필요
graph = [[0]*(n+1) for _ in range(n+1)] 
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

# 연결된 간선을 표시, 1이면 서로 연결되어 있음
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)