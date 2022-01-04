# 수 정렬하기 
# 제한시간 5초
# 메모리 8MB
import sys
from time import time

n = int(sys.stdin.readline())
t0 = time()

num_list = [0]*10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

print(time()-t0)


