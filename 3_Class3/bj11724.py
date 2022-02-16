# 연결 요소의 개수
# S2

'''
[시작 체크 리스트]
 30분 지났으나 발상 불가 또는 아예 다른 길 --> 다른 거 참고
 코드 50% 정도 완성
 30분 보다 더 걸려서 코드 완성
 코드는 다 돌아가는데 효율성에서 걸림
 코드 완성
[완료 후 체크 리스트]
 아예 모르겠음
 중간 정도 이해함
 완벽히 이해함
 '''

import sys
sys.setrecursionlimit(10000) # 파이썬은 재귀 제한이 걸려있음 

def dfs(v):
    visited[v] = True
    for e in adj[v]: # v의 노드들을 꺼냄 
        if not visited[e]: # False + not = True
            dfs(e)

N, M = map(int, input().split()) # 정점의 개수, 간선의 개수
adj = [[] for _ in range(N+1)] # 노드를 저장하는 용도 
visited = [False]*(N+1) # 방문을 체크하는 용도 
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1, N+1):
    if not visited[j]: # False + not  = True
        dfs(j)
        count += 1

print(count)