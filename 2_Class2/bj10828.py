import sys
n = int(sys.stdin.readline())

sta = []
for i in range(n):
    a = sys.stdin.readline().split() 
    # list 형태로 저장 split()을 안 하면 \n까지 포함해서 저장 

    if a[0] == 'push':
        sta.append(a[1])
    if a[0] == 'top':
        if len(sta) == 0:
            print(-1)
        else:
            print(sta[-1])

    if a[0] == 'size':
        print(len(sta))

    if a[0] == 'empty':
        if len(sta) == 0:
            print(1)
        else:
            print(0)
    
    if a[0] == 'pop':
        if len(sta) == 0:
            print(-1)
        else:
            print(sta.pop())
