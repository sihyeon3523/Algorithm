import sys

n = int(input())

grid = [[0]*2]*n

for i in range(n):
    grid[i] = list(map(int, sys.stdin.readline().split()))

grid.sort(key = lambda x: (x[1], x[0]))

for i in grid:
    print(i[0], i[1])
