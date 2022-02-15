# 최대 힙 --> 최소힙 문제에서 -를 해주면 순서가 바뀜 
# 3시 2분 ~ 3시 14분 (최소힙 문제보고 함)
import heapq as hq
import sys

n = int(input())

a = []
for i in range(n):
    x = int(sys.stdin.readline())
    # x가 0일 때 배열에서 가장 큰 값 출력 
    if x == 0:
        if len(a) == 0:
            print(0)
        else:
            print(-hq.heappop(a))

    # x가 0이 아니라면 값 넣어주기 
    else:
        hq.heappush(a, -x)