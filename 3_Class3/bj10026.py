# 빨 파 초

# 적록색약인 사람 = R = G
# 적록색약이 아닌 사람 = R != G
# dfs --> 영역을 카운트 해야함
# 적록색약이 아닌 사람, 적록색약인 사람 
# 3시 45분 ~ 4시 15분

'''
dfs
- visited 리스트가 따로 필요
- 붙어있는 값을 떼어내어 리스트로 만들고 싶을 때 --> list() 하면 된다
- 재귀랑 비슷 
- 같은 거 나오면 재귀함 (다른 거 나올 때까지)
'''
import sys
sys.setrecursionlimit(1000000)

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

three_cnt, two_cnt = 0, 0
dx = [-1, 1, 0, 0] #좌 #우 #위 #아래
dy = [0, 0, -1, 1]

def dfs(a, b):
    visited[a][b] = True
    current_color = graph[a][b]

    for k in range(4):
        nx = a + dx[k]
        ny = b + dy[k]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == False:
                if graph[nx][ny] == current_color:
                    dfs(nx, ny)


# 적록색약이 아닌 사람 
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            three_cnt += 1

# 적록색약인 사람
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            two_cnt += 1

print(three_cnt, two_cnt)
