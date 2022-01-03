'''
from collections import deque

d = deque()
print(type(d))

for i in range(10):
    d.append(i)
print(d) 

d.appendleft(10)
print(d)

d.insert(5,11)
print(d)

d.extend([0,0,0])
print(d)

d.extendleft([0,0,0])
print(d)

for i in range(10):
    d.pop() # 오른쪽에서 요소 삭제 

print(d)

for i in range(3):
    d.popleft()
print(d)

print(list(d))
'''
import sys
from collections import deque

d = deque()

n = int(input())


for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == 'push_front':
        d.appendleft(a[1])
    
    if a[0] == 'push_back':
        d.append(a[1])
    
    if a[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    
    if a[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    
    if a[0] == 'size':
        print(len(d))
    
    if a[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)

    if a[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(list(d)[0])
    if a[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(list(d)[-1])