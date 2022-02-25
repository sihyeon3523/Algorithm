# 절댓값 힙
# 2시 11분 ~ 

# 배열에 정수 넣기
# 절댓값이 가장 작은 값 출력, 제거
# 작은 값이 여러 개라면, 가장 작은 수 출력, 제거 

'''
abs() : 절대값 함수
'''

import sys
import heapq

n = int(input())
q = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])