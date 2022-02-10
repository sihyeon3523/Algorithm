# 최소 힙

# 일종의 트리, 가장 작은 수나 가장 큰 수만을 자주 꺼내올 때 유용
# 완전 이진 트리
# 루트는 가장 작은 값
# 왼쪽 자식= 자신의 인덱스*2, 오른쪽 자식= 자신의 인덱스*2 + 1
# leftchild = parent*2
# rightchild = parent*2 + 1
# parent = child/2
# 들어올 자리의 부모 인덱스와 비교

'''
# 리스트 --> 힙 자료형
heap2 = [50, 10, 20]
heapq.heapify(heap2)
'''

'''
import heapq as hq # 최소 힙 기능만을 동작 (우선순위 큐)


a = [] # 빈 리스트를 생성해줘야 함 
while True:
    n = int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a)) # 루트 노드(최솟값)을 pop
    else:
        hq.heappush(a, n) # 힙의 형태로 알아서 넣어줌 
'''

# 백준 최소 힙 문제풀이
'''
- 배열에 자연수 x를 넣는다
- 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거
'''
import time
start = time.time()

import sys
import heapq as hq

n = int(input())

a = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(a)==0:
            print(0)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, x)

print(time.time()-start)