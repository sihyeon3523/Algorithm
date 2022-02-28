# 단지번호 붙이기
# S1
# BFS
# 각 단지에 속하는 집의 수를 출력 
# 5시 20분 ~ 6시

from collections import deque

# 위치 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# bfs --> 덱
def bfs(i, j):
    q = deque()
    q.append((i, j)) # (i, j) tuple로 묶어서 append 
    graph[i][j] = 0 # 방문 했음을 표시 
    count = 1 # 아파트 수 세기 
    
    while q:
        x, y = q.popleft() 

        # 위치 이동 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 그래프 위에 있는 값이고, 아직 방문하지 않은 아파트이면, q에 append 
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count


n = int(input())

graph = []
for i in range(n):
    # graph의 index를 정해주지 않고 바로 append --> 알아서 index 생성
    graph.append(list(map(int, input())))

cnt = 0 # 단지 수 
hs = [] # 단지별 아파트 수

# 그래프 전체 방문 
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            hs.append(bfs(i, j))
print(cnt)

# 오름차순 정렬 
hs.sort()
for i in hs:
    print(i)