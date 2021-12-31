m = int(input())

for i in range(m):
    h, w, n =  map(int, input().split())
    if (n % h) != 0:
        front = (n % h)*100
        back = n // h + 1
    else:
        front = h*100
        back = n //h 

    print(front+back)