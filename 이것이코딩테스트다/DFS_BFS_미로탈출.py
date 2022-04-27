# 0 : 괴물이 있는 부분
# 1 : 괴물이 없는 부분
# 괴물을 피해서 다녀야 한다
from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)

'''
5 6
101010
111111
000001
111111
111111
'''
# 동빈이가 움직여야 하는 최소 칸의 개수.. 
# 동빈이의 위치는 (1,1)
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1] # 상 하 좌 우

# bfs --> queue
def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록 
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    
    # 가장 오른쪽 아래까지의 최단 거리 반환 
    return graph[n-1][m-1]

print(bfs(0,0))