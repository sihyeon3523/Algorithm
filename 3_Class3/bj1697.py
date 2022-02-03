
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간 
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] +1
                q.append(nx)

n, k = map(int, input().split())

MAX = 10**5
dist = [0]*(MAX+1)

bfs()