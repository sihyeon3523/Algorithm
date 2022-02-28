# 정답코드
import sys
input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans

    # ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
    if ans >= total + max_val*(3-idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    
    # ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
    else:

         # 상, 하, 좌, 우로 이동
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0

                # 방문 표시 및 제거
                visit[nr][nc] = 1
                dfs(nr, nc, idx+1, total+arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0]*M) for _ in range(N)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)

''' 
함수를 따로 지정하지 않는다
같은 함수에 넣고 ㅗ를 구하는 것을 먼저 구한 뒤
계속 비교
안 그러면? 시간초과
어쨌든 다시 풀어야 하고
dfs 문제임을 아는 게 문제였고
dfs를 알더라도 ㅗ의 문제를 해결할 줄 알아야 했다. 
'''
