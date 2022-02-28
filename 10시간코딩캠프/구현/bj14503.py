# 로봇청소기
# G5
# 6시 40분 ~ 7시 50분 

# 빈 칸 0, 벽 1
# 로봇 청소기가 총소하는 칸의 개수
'''
틀렸습니다. ㅠㅠ 
n, m = map(int, input().split()) # 세로, 가로
y, x, d = map(int, input().split()) # 현재 위치: 세로 가로 방향 (북:0, 동:1, 남:2, 서:3 --> 시계방향으로 1씩 증가)
graph = [input().split() for _ in range(n)]

# 방향이 (북, 동, 남, 서)일 때, 왼쪽 이동, 그때의 방향 
dx = [-1, 0, 1, 0] # 서 북 동 남
dy = [0, 1, 0, -1] # 서 북 동 남
dd = [3, 0, 1, 2] # 서 북 동 남 

# 빈 칸=0: 청소해야 할 곳, 벽=1: 청소 못하는 곳 
# 청소를 한 곳은 1로 표시 
graph[x][y] = 1
cnt = 1
for i in range(n):
    for j in range(m):
        for k in range(4):
            tmp = 0
            if d == k:
                nx, ny, nd = x+dx[i], y+dy[i], d+dd[i]
                if (0 <= nx < m) and (0 <= ny < n):
                    # 왼쪽 방향에 아직 청소하지 않은 공간이 존재
                    if graph[nx][ny] == 0:
                        cnt += 1
                        x = nx
                        y = ny
                        d = nd
                        break
                    # 왼쪽 방향에 벽이 존재 혹은 이미 청소한 곳이 존재
                    else:
                        tmp += 1
                        if tmp == 4:

                        x = nx
                        y = ny
                        d = nd     
           
                        break
'''

# 정답 
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1] # 북 동 남 서 

# 현재 좌표와 방향이 입력되면 청소할 수 있는지 확인 
def clean(x, y, d):
    global ans
    # 청소 할 수 있으면 
    if a[x][y] == 0:
        # 0에서 2로 바꾸고 
        a[x][y] = 2
        # ans에 1을 더한다 
        ans += 1

    for  _ in range(4):
        nd = (d+3)%4  # 이동 방향을 문제의 조건대로 북동남서 순으로 만들면 현재 방향 + 3을 4로 나눈 나머지가 왼쪽 방향
        nx = x + dx[nd]
        ny = y + dy[nd]

        # 왼쪽 방향이 0이면
        if a[nx][ny] == 0:
            # clean 함수에 다음 좌표와 방향을 입력
            clean(nx, ny, nd)
            return

        # 4방향 모두 이동할 수 없다면 
        d = nd 
    
    # 뒤로 이동할 수 있는지 확인  
    nd = (d+2)%4 # 현재 방향 + 2를 4로 나눈 나머지가 뒤로 이동
    nx = x + dx[nd]
    ny = y + dy[nd]

    # 뒤가 벽이면 바로 종료 
    if a[nx][ny] == 1:
        return
    # 이동할 수 있으면 다음 좌표와 방향을 입력 
    clean(nx, ny, d) # 바라보는 방향을 유지한 채로 뒤로 이동이기 때문에 nd가 아니라 d

n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
clean(x, y, d)
print(ans)