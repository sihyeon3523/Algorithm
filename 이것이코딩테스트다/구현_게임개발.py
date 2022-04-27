# a : x, b: y

# 8시 42분 ~ 


# 캐릭터가 방문한 칸의 수를 출력

# 바다 = 1, 육지=0

d = [[0]*m  for _ in range(n)]

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d[x][y] = 1

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

#  0 1 2 3 --> 3 0 1 2 
directions = [3, 0, 1, 2]
# 북 동 남 서 일 때 왼쪽 방향 --> 북 동 남 서  = 좌 상 우 하 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전 
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if graph[nx][ny] != 1 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
    else: 
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''