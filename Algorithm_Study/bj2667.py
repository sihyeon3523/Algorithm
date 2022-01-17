'''
bfs 풀이
- 그래프의 탐색 시작점을 모르기 때문에 전체를 돌면서 1인 지점에서 탐색 시작
- 탐색 중 1인 부분은 0으로 바꿔 다시 방문하지 않도록 하고
- 한번 bfs 가 끝나게 되면 더 이상 확장이 불가능 하므로 마을 하나가 탄생 
'''
'''
from collections import deque

dx = [0, 0, 1, -1] # 우 좌 하 상
dy = [1, -1, 0, 0] # 우 좌 하 상

def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0  or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count 
                        

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt  = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
'''

'''
붙어있는 값들을 하나씩 조회/접근 하고 싶을 때 

for i in range(4):
    print(list(input())) # ['2', '3', '4']
    print(list(map(int, input()))) # [2, 3, 4]
'''

'''
dfs
- 그래프의 시작점을 모르기 때문에 전체를 돌면서 1인 지점에서 탐색 시작
- bfs와의 차이점은 큐 대신 재귀로 썼다는 점입니다. 
- 그 외는 위의 bfs 풀이 방식과 동일 
'''
n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] == 1:
        global count 
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False 

count = 0
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(count)
            result += 1
            count = 0

        
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])