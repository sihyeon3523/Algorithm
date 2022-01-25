from collections import deque

m, n = map(int, input().split()) # 가로 # 세로 

# (1) 익은 토마토 (0) 익지 않은 토마토 (-1) 토마토 없음
tomato = []
for i in range(n):
    tomato.append(list(map(int, input().split())))

# 모두 익을 때까지 최소 날짜 출력
# 만약 저장될 때부터 모든 토마토가 익어있는 상태라면 0을 출력
# 토마토가 모두 익지 못하는 상황이면 -1을 출력

dx = [0,0,-1,1]
dy = [1,-1,0,0]

q = deque()

# 토마토 있는 곳은 일단 다 q에 넣어줌 
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
           # bfs(tomato, n, m)
           q.append((i,j))

# bfs로 1 주변에 있는 익지 않은 토마토들 1로 바꿔주면서 
# 시간도 + 1day 해줌 
# 토마토도 익게 하고 날짜도 계산해주면서 tomato 행렬 재정의


'''
def bfs():
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if n > nx >= 0 and m > ny >= 0 and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[a][b] + 1
                q.append((nx, ny))
''' 

def bfs():
    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[a][b] + 1
                q.append((nx, ny))

            if tomato[nx][ny] == -1:
                continue
        # return graph[nx][ny] 할 이유가 없다.. return 할 게 없음

bfs()

# bfs 안에서 어떤 갑싱 최고 값인지 체크하지 말고 
# 밖에서 일자가 몇일인지 체크해줌 
res = 0

# 토마토 행렬에 있는 값들 다 조사 해서
for i in tomato:
    for j in i:
        # 0이 하나라도 있으면 익지 않은 토마토가 있다는 의미이므로
        # -1 출력 
        if j == 0:
            print(-1)
            print(tomato)
            exit(0) # 오류 / 문제없이 깨끗한 출구 exit(1) 문제/오류가 있음을 의미하므로 프로그램이 종료됩니다
    # tomato 행렬 한 줄씩 돌아가면서 max 값(익기까지의 시간) 체크해줌
    res = max(res, max(i))

# 처음 tomato를 받은 날도 포함해서 계산했으므로 -1 해줌 
print(res-1)
# print(tomato)