n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

blue = 0
white = 0

def recur(x, y, n):
    global blue
    global white
    check = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                check = -1
                break
    
    if check == -1:
        n = n//2
        recur(x, y, n) # 왼쪽 위
        recur(x, y+n, n) # 오른쪽 위
        recur(x+n, y, n) # 왼쪽 아래
        recur(x+n, y+n, n) # 오른쪽 아래

    elif check == 1: # 파란 색종이
        blue += 1
    
    elif check == 0:
        white += 1
    
recur(0,0,n)

print(white)
print(blue)