# 같은 크기의 종이 9개 

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

neg = 0
neut = 0
pos = 0

def clip_paper(x, y, n):
    global neg, neut, pos

    # 주어진 테이블이 모두 하나의 기준의 값과 같지 않다면 
    num_check = paper[x][y] 
    for i in range(x, x+n):
        for j in range(y, y+n):
            if (paper[i][j] != num_check):
                # 총 9개로 구분되는 칸으로 나누어 9개의 서브 테이블을 만든다
                for k in range(3):
                    for l in range(3):
                        clip_paper(x+k*n//3, y+l*n//3, n//3)
                return 
    
    # 서브 테이블의 값이 모두 일치할 경우 
    if(num_check == -1):
        neg += 1
    elif(num_check == 0):
        neut += 1
    else:
        pos += 1

clip_paper(0,0,N)
print(f'{neg}\n{neut}\n{pos}')