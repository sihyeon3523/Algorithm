# 한 개의 회의실 
# 회의실 사용표 --> n개의 회의
# 각 회의 i에 대해 시작시간과 끝나는 시간 주어짐
# 회의의 최대 개수 : 한번 시작되면 중간에 중단될 수 없음 
# 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다 
# 최대 사용할 수 있는 회의의 최대 개수
# 4시 40분 ~
# 적은 시간이 걸리는 것을 먼저..?  

import sys

N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    s, e  = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)