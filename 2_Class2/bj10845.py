import sys
n = int(sys.stdin.readline())

q = []

for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        q.append(a[1])

    if a[0] == 'size':
        print(len(q))

    if a[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    
    if a[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
            
    if a[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])


    if a[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    