# 토마토
# G5
# 3차원
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸
# 익은 토마토는 위, 아래, 오른쪽, 왼쪽 토마토에도 영향을 미친다
# 6시 5분 ~ 47분
'''
모든 토마토가 다 익을 때까지 최소 얼마나 걸리냐? 
최소 문제? --> bfs
'''
from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split()) # 가로 m, 세로 n, 높이 h


q = deque() # 익은 토마토 
graph = []
# 높이
for i in range(h):
    floor = []
    # 세로 
    for j in range(n):
        floor.append([*map(int, input().split())])
        # 가로 
        for k in range(m):
            if floor[j][k] == 1:
                q.append((i, j, k))
    graph.append(floor)

# (같은 평면 상에서) 위 아래 왼 오 (다른 평면으로) 위 아래
da = [0, 0, 0, 0, 1, -1] # 높이
db = [1, -1, 0, 0, 0, 0] # 세로 
dc = [0, 0, 1, -1, 0, 0] # 가로 

# bfs로 각 한 칸씩 돈다 
def bfs():
    while q:
        a, b, c = q.popleft()
        # 이동 
        for i in range(6):
            na = a + da[i] # 높이
            nb = b + db[i] # 세로
            nc = c + dc[i] # 가로

            # graph[높이][세로][가로] h n m 
            if 0 <= na < h and 0 <= nb < n and 0 <= nc < m and graph[na][nb][nc] == 0:
                q.append((na, nb, nc))
                graph[na][nb][nc] = graph[a][b][c] + 1

bfs()

# 익지 않은 토마토가 있는지 확인 
result = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0: # 익지 않은 토마토 존재
                print(-1)
                exit() # break 는 가장 가까이에 있는 for문만 종료 시킨다 
        result = max(result, max(j))

# 첫째날은 포함하지 않으므로 -1
print(result-1)
            