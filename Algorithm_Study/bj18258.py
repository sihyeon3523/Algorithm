# 큐 2
# 4시 57분 ~ 5시 13분 

import sys
from collections import deque
input = sys.stdin.readline
q = deque()

n = int(input())

for i in range(n):
    cont = list(input().split())
    
    if cont[0] == 'push':
        q.append(int(cont[1]))
    
    elif cont[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    
    elif cont[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:       
            print(q.popleft())

    elif cont[0] == 'size':
            print(len(q))
    
    elif cont[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif cont[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])