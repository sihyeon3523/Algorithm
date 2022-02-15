# (1,1)에서 (N,M)의 위치로 이동할 때 지나야 하는 최소의 칸 수
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다
# 40분 ~
from collections import deque

n, m = map(int, input().split())
# 최소의 칸 수
# bfs 
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1] # 상 하 좌 우
# (n,m)

def bfs(graph, a, b):
    q = deque() # 방문한 지점을 append 
    q.append((a, b))
    # 이렇게 1을 찾을 때마다 1을 더해준다면 전체 1의 갯수를 출력하는 것이지
    # 미로를 탈출했을 때의 지나온 1의 갯수를 출력해주는 게 아님 
    # 그래서 1이 보일 때마다 count에 1을 더해주면 안된다. 
    # graph[a][b] = 0
    # count += 1 

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽이므로 진행 불가
            if graph[nx][ny] == 0:
                continue

            # 벽이 아니므로 이동 
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                #graph[nx][ny] = 0
                #count += 1
    
    return graph[n-1][m-1]

miro = []
for i in range(n):
    miro.append(list(map(int, input()))) 


print(bfs(miro, 0, 0))
print(miro)