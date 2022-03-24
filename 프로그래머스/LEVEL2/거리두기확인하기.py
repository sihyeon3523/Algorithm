places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


from collections import deque

def bfs(p):
    start = []

    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i,j])

    for s in start:
        queue = deque([s]) # 큐에 초기값
        visited = [[0]*5 for i in range(5)] # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)] # 경로 길이 리스트 
        visited[s[0]][s[1]] = 1
        
        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    
                    # 방문 표시를 하는 이유는? 
                    # 방문 표시를 안하면 주변에 계속 맴돌 수 있다 
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        # distance를 계속 더해주는 방법으로 시작점(사람)과의 거리 구하기 
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1                    

def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))
    return answer

print(solution(places))
'''
1. BFS에서 출발 지점은? 
BFS를 사용하려면 경로 탐색을 시작할 출발점이 필요하다
이 문제에서는 응시자가 앉아있는 자리(P)가 출발 지점이 된다.
P는 없을 수도 있고, 여러개일 수도 있기 때문에 
시작점이 되는 P의 좌표 인덱스를 모두 구해서 start 리스트에 저장한다.

한 응시자라도 거리두기 규칙을 위반했을 때 거리두기는 실패한 것이므로(return 0)
시작점들이 저장되어있는 start 리스트를 반복하며 check 한다. 

이때 start 리스트에 있는 P를 하나씩 BFS 하면서 거리두기 여부 check가
완료되고 나면 '방문 처리' 리스트인 visited, '경로 길이' 리스트인 
distance를 모두 초기화해야 한다. 

2. 빈 테이블('O'), 파티션('X')에 대한 처리는?
P는 BFS 탐색을 시작할 때 다른 P를 만나거나 모든 탐색 가능한 지점을 방문할 때까지
상하좌우 이동을 반복한다. 그렇다면 이동 가능한 위치는 어디일까? 

- 탐색 중 파티션('X')를 만날 때 
P가 파티션('X')을 만나면 이는 벽에 가로막힌 것으로 해당 방향으로는
탐색이 불가능하다. 

- 탐색 중 빈 테이블('O')를 만날 때
빈 테이블('O')은 마찬가지로 열려있는 공간이기 때문에 P가 탐색이
가능하다. 

- 탐색 중 또 다른 'P'를 만날 때
P가 이동을 계속 하다가 또 다른 P를 만나면 경로 거리를 판단해서 맨하튼 
거리 2보다 작으면 거리두기 실패(return 0)을 판단하고 2보다 크면 거리두기 
해당 P는 거리두기 성공을 의미한다. (P가 여러 개일 수 있으니 모든 P의 
시작점에서 BFS 탐색에 성공해야 return 1을 반환해야 함에 주의!)

결과적으로 P의 다음 진행할 위치가 'O'이고 그 지점이 이미 방문하지 않을 곳일
때만 BFS를 진행하면 된다. 
'''