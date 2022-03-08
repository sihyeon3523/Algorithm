# dfs > 재귀
# 한 방향으로 깊이 들어가 끝날 때까지 조사함. 
# 끝나면 배추밭 한 개가 있다고 생각하면 됨.

# recursionError 발생
# 재귀와 관련된 에러이며, 파이썬이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때 발생
# 백준의 채점 서버에서 이 값음 1000으로 되어 있다 (파이썬이 정한 최대 재귀 깊이)
# dfs --> bfs , dp 재귀 --> 반복문으로 해결 
# python이 정한 최대 재귀 깊이를 변경 
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 
    
    if graph[x][y] == 0:
        return
       
    graph[x][y] = 0

    # 자리이동해서 탐색
    dfs(x+1, y) # 아래로 
    dfs(x-1, y) # 위로
    dfs(x, y+1) # 오른쪽
    dfs(x, y-1) # 왼쪽

T = int(input())
for _ in range(T):

    # input 받기 
    m, n, k = map(int, input().split()) # 가로 세로 배추 심어진 위치의 개수

    graph = [[0]*m for _ in range(n)]

# graph[세로인덱스: 행][가로인덱스:열]

    # 배추 심기 
    for i in range(k):
        a, b = map(int, input().split()) # 가로(열), 세로(세로)
        graph[b][a] = 1

    # 주변 값 돌리기 
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1
    
    print(result)

        
