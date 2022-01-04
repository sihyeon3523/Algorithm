# 좌표 정렬하기 
# x좌표가 증가하는 순으로, x좌표가 같다면 y좌표가 증가하는 순서로 정렬
# lambda 함수 이용? sort key 사용하는 거였나.. 뭐더라 

import sys
from time import time

t0 = time()
n = int(input())
grid= [[0]*2]*n

for i in range(n):
    grid[i] = list(map(int, input().split()))

grid.sort(key=lambda x: (x[0], x[1]))

for i in grid:
    print(i[0], i[1])

print(t0 - time())