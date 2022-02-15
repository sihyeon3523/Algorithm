# 11279 최대 힙 S2

import heapq as hq
import sys

n = int(sys.stdin.readline())

a = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not a: # empty --> True 
            print(0)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -x)


# 9095 1,2,3 더하기 S3 --> DP 
n = int(input())

def sol(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return sol(x-1)+sol(x-2)+sol(x-3)

for i in range(n):
    a = int(input())
    print(sol(a))


# 11399 ATM S3 --> 그리디 (짧은 것부터 정렬)
n = int(input())
a = list(map(int, input().split()))
a.sort() # 오름차순

result = 0
for i in range(n+1):
    result += sum(a[:i])

print(result)


# 11723 집합 S5
import sys
n = int(input())
s = set()

for i in range(n):
    a = list(sys.stdin.readline().split())
    
    if a[0] == "add":
        if int(a[1]) in s:
            pass
        else:
            s.add(int(a[1]))
            print(s)

    elif a[0] == "remove":
        s.discard(int(a[1]))

    elif a[0] == "check":
        if int(a[1]) in s:
            print(1)
        else:
            print(0)
    
    elif a[0] == "toggle":
        if int(a[1]) in s:
            s.discard(int(a[1]))
        else:
            s.add(int(a[1]))
    
    elif a[0] == "all":
        s.clear()
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    
    elif a[0] == "empty":
        s.clear()
