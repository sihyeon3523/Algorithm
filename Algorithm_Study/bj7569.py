from collections import deque 
import sys
m, n, h = map(int, input().split()) # 가로 # 세로 # 높이

# m 가로 n 세로 h 높이 

# 가로 3 세로 4 높이 2
a = [[[0]*3 for j in range(4)] for i in range(2)]

# 리스트[높이][세로][가로]
tomato = []
q = deque()
for i in range(h): # 높이
    tmp = []
    for j in range(n): # 세로
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m): # 가로
            if tmp[j][k] == 1:
                q.append([i,j,k])
    tomato.append(tmp)

dx = [0, 0, -1, 1, 0, 0] # 가로: 위 아래 왼 오른 앞 뒤 
dy = [0, 0, 0, 0, 1, -1] # 세로: 위 아래 왼 오른 앞 뒤 
dz = [1, -1, 0, 0, 0, 0] # 높이: 위 아래 왼 오른 앞 뒤 

def bfs():
    while q:
        a, b, c = q.popleft()
        for i in range(6):
            nz = a + dz[i] # 높이
            ny = b + dy[i] # 세로
            nx = c + dx[i] # 가로

            # 리스트[높이][세로][가로] h n m 
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and tomato[nz][ny][nx] == 0:
                q.append([nz, ny, nx])
                tomato[nz][ny][nx] = tomato[a][b][c] + 1

bfs()

res = 0
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        
        res = max(res, max(j))

print(res-1)
