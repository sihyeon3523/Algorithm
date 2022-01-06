# 1 *1*1
# 땅고르기 : 땅의 높이를 일정하게
# N*M

# (2초) 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
# (1초) 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

# 땅의 높이는 256블록을 초과할 수 없다, 음수가 될수 없다

import sys
input = sys.stdin.readline()

n, m, b = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 중간 값을 구성
Min = min(map(min, graph))
Max = max(map(max, graph))
leastTime = 1e9

for i in range(Min, Max+1):
    pluscnt = 0
    minuscnt = 0

    for j in range(n):
        for k in range(m):
            h = graph[j][k] - i
            if h > 0:
                # minusnt = 1번 작업수(인벤토리에 넣기)
                minuscnt += h
            elif h < 0:
                # h가 음수니깐 -를 취해줌으로서 더하기로 바꿔준다
                # pluscnt = 2번 작업 수(인벤토리에서 꺼내어 다시 놓기)
                pluscnt -= h

    if minuscnt+b >= pluscnt:
        time = minuscnt*2 + pluscnt
        if leastTime>= time:
            leastTime = time
            resultHeight = i

print(leastTime, resultHeight)
'''
for i in range(n):t
    for j in range(m):
'''        