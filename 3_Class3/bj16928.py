# 3시 56분 ~
# S1

# 1 ~ 6까지의 수
'''
사다리, 뱀 (내려가)
뱀 < 원래 < 사다리 
목표 : 1번 칸에서 시작해서 100번 칸에 도착하는 것 
모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며,
동시에 두가지를 모두 가지고 있는 경우는 없다 

주사위를 굴려야 하는 횟수의 최솟값 
'''

import sys
from collections import deque

input = sys.stdin.readline

def solve(n,m) :
    
    snake = [0 for _ in range(101)]
    ledder = [0 for k in range(101)]
    #합쳐서 관리하는게 더 나을 것 같다.
    
    visited = [False for _ in range(101)]

    for i in range(n) :
        x , y = map(int,input().split())
        ledder[x] = y
    
    for j in range(m) :
        x , y = map(int,input().split())
        snake[x] = y

    q = deque()

    q.append((1,0))
    visited[1] = True

    ans = float("inf")

    while q :
        
        front = q.popleft()

        if front[0] == 100 :
            ans = min(ans, front[1])
            continue


        for i in range(1,7) :
            new = front[0]+i
            
            if new > 100 :continue
            
            if visited[new] == True :
                continue
            
            visited[new] = True

            if snake[new] != 0 :
                new = snake[new]
            
            if ledder[new] != 0 :
                new = ledder[new]

            q.append((new,front[1]+1))
    
    print(ans)

# __name__ 인터프리터가 실행 전에 만들어 둔 글로벌 변수입니다.
if __name__ =="__main__" : # 인터프리터가 직접 실행했을 경우에만 if문 내의 코드를 돌려라 
    n,m = map(int,input().split())
    solve(n,m)