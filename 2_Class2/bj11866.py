from collections import deque

q = deque()
num = []

n, k = map(int, input().split())

for i in range(1, n+1):
    q.append(i)

while q:
    for i in range(k-1):
        q.append(q.popleft())
    num.append(q.popleft())

print("<", end = '')

for i in range(len(num)-1):
    print("%d,"%num[i], end='')

print(num[-1], end='')
print(">")
